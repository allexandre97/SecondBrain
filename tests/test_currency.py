#!/usr/bin/env python3
"""Tests for page currency rules and the set_currency tool."""

from __future__ import annotations

import contextlib
import io
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS))

import set_currency  # noqa: E402
import wiki_search  # noqa: E402
from wiki_currency import BANNER_PREFIX, currency_issues, index_marker_issues  # noqa: E402
from wiki_markdown import parse_frontmatter  # noqa: E402

TODAY = date(2026, 10, 11)
PROJECT_PAGE = """---
type: answer
status: active
updated: 2026-10-01
project_evidence:
  - "Repository audit on 2026-10-01"
---
# Gate Policy

The gates decide each step.

## Details

overlapgatetoken
"""


def issues(text: str) -> tuple[list[str], list[str]]:
    frontmatter, body = parse_frontmatter(text)
    return currency_issues(frontmatter, body, TODAY)


def page(frontmatter: str, body: str = "# Title\n\nBody.\n") -> str:
    return f"---\ntype: concept\n{frontmatter}---\n{body}"


class CurrencyRuleTests(unittest.TestCase):
    def test_timeless_page_without_fields_is_valid(self) -> None:
        self.assertEqual(issues(page("")), ([], []))

    def test_answer_pages_require_explicit_scope(self) -> None:
        answer = "---\ntype: answer\n---\n# Answer\n"
        self.assertTrue(any("must declare scope" in error for error in issues(answer)[0]))
        self.assertEqual(issues(answer.replace("type: answer\n", "type: answer\nscope: timeless\n"))[0], [])

    def test_index_markers_must_match_page_currency(self) -> None:
        index = [
            "- [[wiki/answers/old]] - Gate policy.",
            "- [[wiki/answers/new]] - **Superseded:** Replacement.",
            "- [[overview]] - Overview.",
        ]
        currency = {"wiki/answers/old": "superseded", "wiki/answers/new": "current"}
        errors = index_marker_issues(index, currency)
        self.assertEqual(len(errors), 2)
        self.assertIn("**Superseded:**", errors[0])
        self.assertIn("not carry", errors[1])
        fixed = ["- [[wiki/answers/old]] - **Superseded:** Gate policy.", "- [[wiki/answers/new]] - Replacement."]
        self.assertEqual(index_marker_issues(fixed, currency), [])

    def test_project_evidence_requires_explicit_scope(self) -> None:
        errors, _ = issues(PROJECT_PAGE)
        self.assertTrue(any("must declare scope" in error for error in errors))
        errors, _ = issues(PROJECT_PAGE.replace("status: active\n", "status: active\nscope: timeless\n"))
        self.assertEqual(errors, [])

    def test_time_bound_pages_need_currency_and_as_of(self) -> None:
        errors, _ = issues(page("scope: snapshot\n"))
        self.assertTrue(any("must declare currency" in error for error in errors))
        self.assertTrue(any("must declare as_of" in error for error in errors))

    def test_invalid_values_are_errors(self) -> None:
        errors, _ = issues(
            page("scope: snapshot\ncurrency: stale\nas_of: 1 Oct\nas_of_commit:\n  - FFRefine-6b20031\n")
        )
        self.assertEqual(len(errors), 3)
        errors, _ = issues(page("scope: living\ncurrency: historical\nas_of: 2026-10-01\n",
                                f"# T\n\n{BANNER_PREFIX} Historical\n"))
        self.assertTrue(any("living page cannot be historical" in error for error in errors))

    def test_superseded_page_needs_replacement_and_banner(self) -> None:
        errors, _ = issues(page("scope: snapshot\ncurrency: superseded\nas_of: 2026-10-01\n"))
        self.assertTrue(any("superseded_by" in error for error in errors))
        self.assertTrue(any("banner" in error for error in errors))
        errors, _ = issues(page(
            'scope: snapshot\ncurrency: superseded\nas_of: 2026-10-01\nsuperseded_by:\n  - "[[wiki/answers/new]]"\n',
            f"# T\n\n{BANNER_PREFIX} Superseded\n\nBody.\n",
        ))
        self.assertEqual(errors, [])

    def test_banner_on_current_page_is_an_error(self) -> None:
        errors, _ = issues(page(
            "scope: snapshot\ncurrency: current\nas_of: 2026-10-01\n", f"# T\n\n{BANNER_PREFIX} Historical\n"
        ))
        self.assertTrue(any("not historical or superseded" in error for error in errors))

    def test_impossible_as_of_date_is_an_error_not_a_crash(self) -> None:
        errors, _ = issues(page("scope: living\ncurrency: current\nas_of: 2026-02-30\n"))
        self.assertTrue(any("valid YYYY-MM-DD" in error for error in errors))

    def test_heading_inside_code_fence_is_not_the_h1(self) -> None:
        body = f"Intro\n\n```bash\n# comment\n{BANNER_PREFIX} Historical\n```\n"
        errors, _ = issues(page("scope: snapshot\ncurrency: historical\nas_of: 2026-10-01\n", body))
        self.assertTrue(any("banner" in error for error in errors))

    def test_living_page_warnings(self) -> None:
        errors, warnings = issues(page(
            "scope: living\ncurrency: current\nas_of: 2026-06-01\n",
            "# T\n\n## 2026-10-11 update: removals\n\nText.\n",
        ))
        self.assertEqual(errors, [])
        self.assertEqual(len(warnings), 2)


class SetCurrencyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name).resolve()
        (self.root / "wiki" / "answers").mkdir(parents=True)
        self.old = self.root / "wiki" / "answers" / "old.md"
        self.old.write_text(PROJECT_PAGE, encoding="utf-8")
        (self.root / "wiki" / "answers" / "new.md").write_text(page("scope: living\n"), encoding="utf-8")
        self.index = self.root / "wiki" / "index.md"
        self.index.write_text(
            "# Wiki Index\n\n- [[wiki/answers/old]] - Gate policy.\n- [[wiki/answers/new]] - Replacement.\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def run_tool(self, *args: str) -> int:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return set_currency.main(["wiki/answers/old.md", *args], root=self.root)

    def test_snapshot_supersede_and_restore_round_trip(self) -> None:
        self.assertEqual(
            self.run_tool("--scope", "snapshot", "--currency", "current", "--as-of", "2026-10-01",
                          "--as-of-commit", "FFRefine@6b20031"),
            0,
        )
        text = self.old.read_text(encoding="utf-8")
        self.assertEqual(issues(text)[0], [])
        self.assertNotIn(BANNER_PREFIX, text)
        self.assertIn("project_evidence:\n  - \"Repository audit on 2026-10-01\"", text)

        for _ in range(2):  # repeating the call must not duplicate the banner
            self.assertEqual(self.run_tool("--superseded-by", "[[wiki/answers/new]]", "--note", "Gates retired."), 0)
        text = self.old.read_text(encoding="utf-8")
        self.assertEqual(issues(text)[0], [])
        self.assertEqual(text.count(BANNER_PREFIX), 1)
        self.assertIn('superseded_by:\n  - "[[wiki/answers/new]]"', text)
        self.assertIn("# Gate Policy\n\n> [!currency] Superseded — describes the state as of 2026-10-01 "
                      "(FFRefine@6b20031). Current information: [[wiki/answers/new]]\n> Gates retired.\n\n"
                      "The gates decide each step.", text)

        self.assertIn("- [[wiki/answers/old]] - **Superseded:** Gate policy.\n", self.index.read_text(encoding="utf-8"))

        self.assertEqual(self.run_tool("--currency", "current"), 0)
        self.assertIn("- [[wiki/answers/old]] - Gate policy.\n", self.index.read_text(encoding="utf-8"))
        text = self.old.read_text(encoding="utf-8")
        self.assertEqual(issues(text)[0], [])
        self.assertNotIn(BANNER_PREFIX, text)
        self.assertNotIn("superseded_by", text)
        self.assertIn("# Gate Policy\n\nThe gates decide each step.", text)

    def test_clear_currency_turns_living_page_timeless(self) -> None:
        self.run_tool("--scope", "living", "--currency", "current", "--as-of", "2026-10-01")
        self.assertEqual(self.run_tool("--scope", "timeless"), 1)  # timeless pages cannot be current
        self.assertEqual(self.run_tool("--scope", "timeless", "--clear-currency"), 0)
        frontmatter, _ = parse_frontmatter(self.old.read_text(encoding="utf-8"))
        self.assertEqual(frontmatter["scope"], "timeless")
        self.assertFalse({"currency", "as_of", "as_of_commit", "superseded_by"} & set(frontmatter))

    def test_invalid_requests_leave_page_unchanged(self) -> None:
        self.assertEqual(self.run_tool("--scope", "snapshot"), 1)  # missing currency and as_of
        self.assertEqual(self.run_tool("--superseded-by", "wiki/answers/missing"), 1)
        self.assertEqual(self.run_tool("--superseded-by", "wiki/answers/old"), 1)  # itself
        self.assertEqual(self.run_tool("--scope", "snapshot", "--as-of", "2026-10-01", "--currency", "current",
                                       "--superseded-by", "wiki/answers/new"), 1)
        self.assertEqual(self.run_tool("--scope", "living", "--currency", "current", "--as-of", "2026-02-30"), 1)
        # Without --scope, an unmigrated project page must not gain a default scope.
        self.assertEqual(self.run_tool("--currency", "historical", "--as-of", "2026-10-01"), 1)
        self.assertEqual(self.old.read_text(encoding="utf-8"), PROJECT_PAGE)

    def test_note_survives_later_edits_without_note(self) -> None:
        self.run_tool("--scope", "snapshot", "--currency", "historical", "--as-of", "2026-10-01",
                      "--note", "Reason here.")
        self.assertEqual(self.run_tool("--as-of-commit", "FFRefine@abcdef1"), 0)
        text = self.old.read_text(encoding="utf-8")
        self.assertIn("(FFRefine@abcdef1); kept as a record, not as the current state.\n> Reason here.\n", text)

    def test_blank_line_inside_managed_list_is_removed_with_its_key(self) -> None:
        self.old.write_text(PROJECT_PAGE.replace(
            "updated: 2026-10-01\n",
            'updated: 2026-10-01\nscope: snapshot\ncurrency: superseded\nas_of: 2026-10-01\n'
            'superseded_by:\n\n  - "[[wiki/answers/new]]"\n',
        ).replace("# Gate Policy\n", f"# Gate Policy\n\n{BANNER_PREFIX} Superseded\n"), encoding="utf-8")
        self.assertEqual(self.run_tool("--currency", "current"), 0)
        frontmatter, _ = parse_frontmatter(self.old.read_text(encoding="utf-8"))
        self.assertNotIn("superseded_by", frontmatter)
        self.assertIsInstance(frontmatter["updated"], str)

    def test_search_reports_currency_and_filters_non_current(self) -> None:
        self.run_tool("--scope", "snapshot", "--as-of", "2026-10-01", "--superseded-by", "wiki/answers/new")
        result = wiki_search.search(self.root, "overlapgatetoken").results[0]
        self.assertEqual(
            (result["scope"], result["currency"], result["as_of"], result["superseded_by"]),
            ("snapshot", "superseded", "2026-10-01", ["wiki/answers/new"]),
        )
        self.assertFalse(wiki_search.search(self.root, "overlapgatetoken", current_only=True).results)
        self.assertEqual(wiki_search.search(self.root, "Body", current_only=True).results[0]["currency"], None)


if __name__ == "__main__":
    unittest.main()
