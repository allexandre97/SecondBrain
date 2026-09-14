#!/usr/bin/env python3
"""Tests for deterministic SQLite FTS5 wiki search."""

from __future__ import annotations

import contextlib
import io
import json
import sqlite3
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest import mock

TOOLS = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS))

import search_wiki  # noqa: E402
import wiki_search  # noqa: E402


class WikiSearchTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        (self.root / "wiki" / "concepts").mkdir(parents=True)
        (self.root / "wiki" / "sources").mkdir(parents=True)
        self.write(
            "wiki/concepts/free-energy.md",
            """---
type: concept
status: active
display_title: Free Energy Methods
short_title: FE Methods
aliases:
  - FEP
  - Alchemical perturbation
categories:
  - research/molecular-simulation/free-energy
tags: [thermodynamics, methods]
sources:
  - SRC-9001
---
# Free Energy Estimation

A baseline introduction mentions ordinary corpus language.

## Reweighting

The overlapneedle estimator reweights sampled configurations.

## Diagnostics

The overlapneedle diagnostic checks effective sample size.

```markdown
# Not a real heading
```
""",
        )
        self.write(
            "wiki/sources/source.md",
            """---
type: source
status: complete
source_id: SRC-9001
display_title: Experimental Observable Collection
short_title: Observable Collection
aliases: [EOC, Garnet observables]
categories:
  - research/molecular-simulation/data
---
# Measurements for Garnet

Observed density and hydration values support force field optimization.
""",
        )
        self.write(
            "wiki/concepts/body-only.md",
            """---
type: concept
categories: []
---
# Secondary Note

This body discusses FEP and free energy estimation in passing.
""",
        )
        self.write(
            "wiki/concepts/generated.md",
            """---
type: concept
generated: true
---
# Generated Navigation

uniquenavigationtoken
""",
        )
        self.write("wiki/plain.md", "# Plain Page\n\nmissingmetadata token\n")
        self.write("wiki/malformed.md", "---\ntype: concept\n# Malformed Heading\nmalformedtoken\n")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write(self, relative: str, text: str) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def search(self, query: str, **kwargs: object) -> wiki_search.SearchResponse:
        return wiki_search.search(self.root, query, **kwargs)

    def correct(
        self, query: str, *, include_generated: bool = False
    ) -> tuple[list[str], list[dict[str, object]]]:
        database = wiki_search.ensure_index(self.root, include_generated)
        connection = sqlite3.connect(database)
        try:
            return wiki_search.fuzzy_correct_tokens(
                connection, wiki_search.query_tokens(query)
            )
        finally:
            connection.close()

    def test_index_creation_and_relative_paths(self) -> None:
        database = wiki_search.ensure_index(self.root)
        self.assertTrue(database.is_file())
        connection = sqlite3.connect(database)
        paths = [row[0] for row in connection.execute("SELECT path FROM pages ORDER BY path")]
        connection.close()
        self.assertIn("wiki/concepts/free-energy.md", paths)
        self.assertTrue(all(not Path(path).is_absolute() for path in paths))

    def test_body_title_display_alias_heading_and_source_matches(self) -> None:
        cases = {
            "ordinary corpus": "wiki/concepts/free-energy.md",
            "Free Energy Estimation": "wiki/concepts/free-energy.md",
            "Free Energy Methods": "wiki/concepts/free-energy.md",
            "FEP": "wiki/concepts/free-energy.md",
            "Reweighting": "wiki/concepts/free-energy.md",
            "SRC-9001": "wiki/sources/source.md",
        }
        for query, expected in cases.items():
            with self.subTest(query=query):
                self.assertEqual(self.search(query).results[0]["path"], expected)

    def test_weighted_fields_rank_title_alias_heading_over_body(self) -> None:
        self.write("wiki/concepts/a-title.md", "# rankneedle\n\nneutral text\n")
        self.write("wiki/concepts/b-alias.md", "---\naliases: [rankneedle]\n---\n# Neutral Alias\n\nneutral text\n")
        self.write("wiki/concepts/c-heading.md", "# Neutral Heading\n\n## rankneedle\n\nneutral text\n")
        self.write("wiki/concepts/d-body.md", "# Neutral Body\n\nrankneedle text\n")
        response = self.search("rankneedle", limit=10, per_page=1, rebuild=True)
        selected = [
            item["path"]
            for item in response.results
            if item["path"].startswith("wiki/concepts/")
            and Path(item["path"]).name[0] in {"a", "b", "c", "d"}
        ]
        self.assertEqual(
            selected,
            [
                "wiki/concepts/a-title.md",
                "wiki/concepts/b-alias.md",
                "wiki/concepts/c-heading.md",
                "wiki/concepts/d-body.md",
            ],
        )

    def test_alias_match_is_strong(self) -> None:
        results = self.search("FEP", limit=5, per_page=1).results
        self.assertEqual(results[0]["path"], "wiki/concepts/free-energy.md")
        self.assertGreater(results[0]["score"], results[1]["score"])

    def test_sections_are_separate_and_page_is_capped(self) -> None:
        response = self.search("overlapneedle", limit=10)
        sections = [item["section"] for item in response.results]
        self.assertEqual(sections, ["Reweighting", "Diagnostics"])
        self.assertTrue(all("Not a real heading" not in (item["section_path"] or "") for item in response.results))

    def test_page_cap_does_not_hide_lower_ranked_pages(self) -> None:
        many_sections = "# Dominant\n" + "\n".join(
            f"## Section {number}\ncapneedle capneedle capneedle" for number in range(250)
        )
        self.write("wiki/concepts/dominant.md", many_sections)
        for number in range(10):
            self.write(
                f"wiki/concepts/alternative-{number}.md",
                f"# Alternative {number}\n\ncapneedle\n",
            )
        results = self.search("capneedle", limit=10, rebuild=True).results
        self.assertEqual(len(results), 10)
        self.assertLessEqual(
            sum(item["path"] == "wiki/concepts/dominant.md" for item in results), 2
        )

    def test_title_only_match_does_not_mistake_wikilink_for_highlight(self) -> None:
        self.write(
            "wiki/concepts/title-snippet.md",
            "# titleonlyneedle\n\nUnrelated [[wiki/concepts/free-energy]] body text.\n",
        )
        result = self.search("titleonlyneedle", rebuild=True).results[0]
        self.assertIn("⟦titleonlyneedle⟧", result["snippet"])
        self.assertNotIn("Unrelated", result["snippet"])

    def test_structured_filters(self) -> None:
        self.assertTrue(self.search("energy", page_type="concept").results)
        self.assertFalse(self.search("energy", page_type="source").results)
        self.assertTrue(
            self.search(
                "energy", category="research/molecular-simulation/free-energy"
            ).results
        )
        self.assertFalse(self.search("energy", category="research/molecular-simulation").results)
        self.assertEqual(
            self.search("energy", path="concepts/free").results[0]["path"],
            "wiki/concepts/free-energy.md",
        )
        self.assertTrue(self.search("estimation", status="active").results)
        self.assertTrue(self.search("estimation", source="SRC-9001").results)
        self.assertTrue(self.search("estimation", tag="thermodynamics").results)

    def test_deterministic_order_and_tie_breaking(self) -> None:
        self.write("wiki/concepts/tie-b.md", "# Tie B\n\ntieuniquetoken\n")
        self.write("wiki/concepts/tie-a.md", "# Tie A\n\ntieuniquetoken\n")
        first = self.search("tieuniquetoken", rebuild=True).results
        second = self.search("tieuniquetoken").results
        self.assertEqual(first, second)
        self.assertEqual([item["path"] for item in first], ["wiki/concepts/tie-a.md", "wiki/concepts/tie-b.md"])

    def test_safe_query_and_and_then_or_behavior(self) -> None:
        and_response = self.search('ordinary, corpus! "language"')
        self.assertEqual(and_response.match_mode, "and")
        self.assertEqual(and_response.results[0]["path"], "wiki/concepts/free-energy.md")
        or_response = self.search("overlapneedle impossibleterm")
        self.assertEqual(or_response.match_mode, "or")
        self.assertTrue(or_response.results)
        self.assertEqual(self.search("SRC-9001 (FEP) +").match_mode, "and")

    def test_generated_pages_are_optional(self) -> None:
        self.assertFalse(self.search("uniquenavigationtoken").results)
        included = self.search("uniquenavigationtoken", include_generated=True)
        self.assertEqual(included.results[0]["path"], "wiki/concepts/generated.md")
        self.assertNotEqual(
            wiki_search.index_path(self.root), wiki_search.index_path(self.root, True)
        )

    def test_generated_only_content_change_does_not_stale_default_index(self) -> None:
        default_database = wiki_search.ensure_index(self.root)
        generated_database = wiki_search.ensure_index(self.root, include_generated=True)
        default_mtime = default_database.stat().st_mtime_ns
        generated_mtime = generated_database.stat().st_mtime_ns

        self.write(
            "wiki/concepts/generated.md",
            """---
type: concept
generated: true
---
# Changed Generated Navigation

changednavigationtoken with additional generated content
""",
        )

        self.assertFalse(wiki_search.index_is_stale(self.root))
        self.assertTrue(wiki_search.index_is_stale(self.root, include_generated=True))
        wiki_search.ensure_index(self.root)
        self.assertEqual(default_database.stat().st_mtime_ns, default_mtime)
        self.assertEqual(generated_database.stat().st_mtime_ns, generated_mtime)
        self.assertFalse(self.search("changednavigationtoken").results)
        self.assertTrue(
            self.search("changednavigationtoken", include_generated=True).results
        )

    def test_generated_page_becoming_handwritten_stales_default_index(self) -> None:
        wiki_search.ensure_index(self.root)
        self.write(
            "wiki/concepts/generated.md",
            """---
type: concept
---
# Formerly Generated Page

newlyindexedtoken
""",
        )
        self.assertTrue(wiki_search.index_is_stale(self.root))
        result = self.search("newlyindexedtoken").results[0]
        self.assertEqual(result["path"], "wiki/concepts/generated.md")

    def test_handwritten_page_becoming_generated_stales_default_index(self) -> None:
        wiki_search.ensure_index(self.root)
        self.write(
            "wiki/plain.md",
            """---
generated: true
---
# Plain Page

missingmetadata token
""",
        )
        self.assertTrue(wiki_search.index_is_stale(self.root))
        self.assertFalse(self.search("missingmetadata").results)

    def test_missing_and_malformed_frontmatter_are_safe(self) -> None:
        self.assertEqual(self.search("missingmetadata").results[0]["path"], "wiki/plain.md")
        self.assertEqual(self.search("malformedtoken").results[0]["path"], "wiki/malformed.md")

    def test_unusual_headings_and_fenced_heading(self) -> None:
        self.write(
            "wiki/concepts/headings.md",
            "# C# language\n\n### Deep heading ###\ncontent\n\n####### not-a-heading\n",
        )
        _title, sections = wiki_search.parse_sections(
            (self.root / "wiki/concepts/headings.md").read_text().splitlines()
        )
        self.assertEqual(sections[0].heading, "C# language")
        self.assertEqual(sections[1].heading, "Deep heading")
        self.assertIn("####### not-a-heading", sections[1].body)
        _title, fenced = wiki_search.parse_sections(
            "# Page\n\n```python\n```` not a close\n# still code\n```\n## Real section\n".splitlines()
        )
        self.assertEqual([section.heading for section in fenced], ["Page", "Real section"])

    def test_content_change_rebuilds_but_unchanged_index_is_reused(self) -> None:
        database = wiki_search.ensure_index(self.root)
        initial_mtime = database.stat().st_mtime_ns
        self.assertFalse(wiki_search.index_is_stale(self.root))
        wiki_search.ensure_index(self.root)
        self.assertEqual(database.stat().st_mtime_ns, initial_mtime)
        time.sleep(0.01)
        self.write("wiki/plain.md", "# Plain Page\n\nupdatedsearchtoken\n")
        self.assertTrue(wiki_search.index_is_stale(self.root))
        self.assertEqual(self.search("updatedsearchtoken").results[0]["path"], "wiki/plain.md")
        self.assertFalse(self.search("missingmetadata").results)

    def test_one_character_typo_is_corrected(self) -> None:
        response = self.search("reweigting")
        self.assertTrue(response.fuzzy)
        self.assertEqual(response.effective_query, "reweighting")
        self.assertEqual(
            response.corrections,
            [{"original": "reweigting", "corrected": "reweighting", "distance": 1}],
        )
        self.assertEqual(response.results[0]["path"], "wiki/concepts/free-energy.md")

    def test_two_character_typo_is_corrected_for_long_term(self) -> None:
        response = self.search("overlapneedxx")
        self.assertTrue(response.fuzzy)
        self.assertEqual(response.effective_query, "overlapneedle")
        self.assertEqual(response.corrections[0]["distance"], 2)

    def test_known_term_is_never_changed_even_in_explicit_mode(self) -> None:
        response = self.search("Reweighting", fuzzy=True)
        self.assertFalse(response.fuzzy)
        self.assertEqual(response.effective_query, "Reweighting")
        self.assertEqual(response.corrections, [])
        self.assertTrue(response.results)

    def test_fuzzy_vocabulary_uses_fts_diacritic_normalization(self) -> None:
        self.write("wiki/concepts/accent.md", "# Kubincová method\n\naccented title\n")
        response = self.search("kubincova", fuzzy=True)
        self.assertFalse(response.fuzzy)
        self.assertTrue(response.results)
        database = wiki_search.ensure_index(self.root)
        connection = sqlite3.connect(database)
        try:
            self.assertEqual(
                connection.execute(
                    "SELECT priority FROM fuzzy_terms WHERE term = 'kubincova'"
                ).fetchone(),
                (wiki_search.FUZZY_PRIORITY_TITLE_OR_ALIAS,),
            )
        finally:
            connection.close()

    def test_short_unknown_token_is_not_corrected(self) -> None:
        response = self.search("FEQ", fuzzy=True)
        self.assertFalse(response.fuzzy)
        self.assertEqual(response.effective_query, "FEQ")
        self.assertFalse(response.results)

    def test_candidate_outside_maximum_edit_distance_is_rejected(self) -> None:
        self.write("wiki/concepts/distance.md", "# Qzxvw\n\nneutral text\n")
        corrected, corrections = self.correct("qazxy")
        self.assertEqual(corrected, ["qazxy"])
        self.assertEqual(corrections, [])
        self.assertEqual(wiki_search.maximum_edit_distance(5), 1)

    def test_title_priority_breaks_equal_distance_tie(self) -> None:
        self.write("wiki/concepts/priority-title.md", "# qazplumz\n\nneutral text\n")
        self.write("wiki/concepts/priority-body.md", "# Neutral Priority\n\nqazpluma\n")
        corrected, _corrections = self.correct("qazplumx")
        self.assertEqual(corrected, ["qazplumz"])

    def test_alias_is_a_high_priority_fuzzy_candidate(self) -> None:
        self.write(
            "wiki/concepts/alias-priority.md",
            "---\naliases: [vexneedlz]\n---\n# Neutral Alias Candidate\n\nneutral\n",
        )
        self.write("wiki/concepts/alias-body.md", "# Neutral Body Candidate\n\nvexneedla\n")
        corrected, _corrections = self.correct("vexneedlx")
        self.assertEqual(corrected, ["vexneedlz"])

    def test_document_frequency_breaks_candidate_tie(self) -> None:
        self.write("wiki/concepts/df-a.md", "# Frequency One\n\ndfneedlz\n")
        self.write("wiki/concepts/df-b.md", "# Frequency Two\n\ndfneedlz\n")
        self.write("wiki/concepts/df-c.md", "# Frequency Three\n\ndfneedla\n")
        corrected, _corrections = self.correct("dfneedlx")
        self.assertEqual(corrected, ["dfneedlz"])

    def test_lexical_order_breaks_complete_candidate_tie(self) -> None:
        self.write("wiki/concepts/lex-a.md", "# Lexical One\n\nlexneedla\n")
        self.write("wiki/concepts/lex-z.md", "# Lexical Two\n\nlexneedlz\n")
        corrected, _corrections = self.correct("lexneedlx")
        self.assertEqual(corrected, ["lexneedla"])

    def test_automatic_fuzzy_fallback_only_runs_after_empty_lexical_search(self) -> None:
        typo = self.search("reweigting")
        self.assertEqual(typo.match_mode, "fuzzy-and")
        with mock.patch.object(
            wiki_search,
            "fuzzy_correct_tokens",
            side_effect=AssertionError("fuzzy fallback should not run"),
        ):
            exact = self.search("reweighting")
        self.assertFalse(exact.fuzzy)
        self.assertEqual(exact.match_mode, "and")

    def test_explicit_fuzzy_forces_correction_after_partial_lexical_match(self) -> None:
        automatic = self.search("reweigthing overlapneedle")
        self.assertFalse(automatic.fuzzy)
        self.assertEqual(automatic.match_mode, "or")
        forced = self.search("reweigthing overlapneedle", fuzzy=True)
        self.assertTrue(forced.fuzzy)
        self.assertEqual(forced.effective_query, "reweighting overlapneedle")
        self.assertEqual(forced.match_mode, "fuzzy-and")

    def test_corrected_query_uses_or_fallback_when_corrected_and_is_empty(self) -> None:
        response = self.search("reweigting garnat")
        self.assertTrue(response.fuzzy)
        self.assertEqual(response.effective_query, "reweighting garnet")
        self.assertEqual(response.match_mode, "fuzzy-or")
        self.assertTrue(response.results)

    def test_no_fuzzy_disables_automatic_fallback(self) -> None:
        response = self.search("reweigting", fuzzy=False)
        self.assertFalse(response.fuzzy)
        self.assertEqual(response.effective_query, "reweigting")
        self.assertFalse(response.results)

    def test_cli_fuzzy_and_no_fuzzy_modes(self) -> None:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = search_wiki.main(
                ["reweigthing", "overlapneedle", "--fuzzy", "--json"], root=self.root
            )
        self.assertEqual(code, 0)
        self.assertTrue(json.loads(output.getvalue())["fuzzy"])

        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = search_wiki.main(["reweigting", "--no-fuzzy", "--json"], root=self.root)
        self.assertEqual(code, 0)
        payload = json.loads(output.getvalue())
        self.assertFalse(payload["fuzzy"])
        self.assertFalse(payload["results"])

    def test_conflicting_fuzzy_cli_flags_fail_cleanly(self) -> None:
        error = io.StringIO()
        with contextlib.redirect_stderr(error), self.assertRaises(SystemExit) as raised:
            search_wiki.main(["query", "--fuzzy", "--no-fuzzy"], root=self.root)
        self.assertEqual(raised.exception.code, 2)
        self.assertIn("not allowed with argument", error.getvalue())

    def test_json_cli_is_clean_and_has_required_fields(self) -> None:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = search_wiki.main(["reweigting", "--json"], root=self.root)
        self.assertEqual(code, 0)
        payload = json.loads(output.getvalue())
        self.assertEqual(payload["query"], "reweigting")
        self.assertEqual(payload["effective_query"], "reweighting")
        self.assertTrue(payload["fuzzy"])
        self.assertEqual(payload["match_mode"], "fuzzy-and")
        self.assertEqual(payload["corrections"][0]["distance"], 1)
        result = payload["results"][0]
        for field in ("path", "title", "section", "score", "snippet", "type", "categories"):
            self.assertIn(field, result)

    def test_json_reports_no_correction_for_successful_exact_query(self) -> None:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = search_wiki.main(["Garnet", "observables", "--json"], root=self.root)
        self.assertEqual(code, 0)
        payload = json.loads(output.getvalue())
        self.assertEqual(payload["query"], "Garnet observables")
        self.assertEqual(payload["effective_query"], "Garnet observables")
        self.assertFalse(payload["fuzzy"])
        self.assertEqual(payload["corrections"], [])

    def test_human_output_reports_compact_fuzzy_correction(self) -> None:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = search_wiki.main(["reweigting"], root=self.root)
        self.assertEqual(code, 0)
        self.assertEqual(output.getvalue().splitlines()[0], "Fuzzy correction: reweigting → reweighting")

    def test_fuzzy_search_results_are_normal_bm25_results(self) -> None:
        self.write("wiki/concepts/rank-title.md", "# rankneedle\n\nneutral text\n")
        self.write("wiki/concepts/rank-body.md", "# Neutral Rank\n\nrankneedle text\n")
        fuzzy = self.search("rankneedlf", limit=10, per_page=1, rebuild=True)
        exact = self.search("rankneedle", limit=10, per_page=1)
        self.assertTrue(fuzzy.fuzzy)
        self.assertEqual(fuzzy.results, exact.results)
        self.assertEqual(fuzzy.results[0]["path"], "wiki/concepts/rank-title.md")

    def test_metadata_filters_continue_to_apply_exactly(self) -> None:
        matched = self.search(
            "estimatiox",
            page_type="concept",
            category="research/molecular-simulation/free-energy",
            source="SRC-9001",
            tag="thermodynamics",
        )
        self.assertTrue(matched.fuzzy)
        self.assertEqual(matched.results[0]["path"], "wiki/concepts/free-energy.md")
        self.assertFalse(self.search("estimatiox", page_type="source").results)
        self.assertFalse(self.search("estimatiox", tag="thermodynamic").results)

    def test_generated_pages_have_separate_fuzzy_vocabularies(self) -> None:
        typo = "uniquenavigationtokeq"
        default = self.search(typo, fuzzy=True)
        self.assertFalse(default.fuzzy)
        self.assertFalse(default.results)
        included = self.search(typo, include_generated=True, fuzzy=True)
        self.assertTrue(included.fuzzy)
        self.assertEqual(included.effective_query, "uniquenavigationtoken")
        self.assertEqual(included.results[0]["path"], "wiki/concepts/generated.md")

    def test_fuzzy_vocabulary_updates_with_corpus_manifest(self) -> None:
        database = wiki_search.ensure_index(self.root)
        connection = sqlite3.connect(database)
        try:
            self.assertIsNone(
                connection.execute(
                    "SELECT term FROM fuzzy_terms WHERE term = 'refreshneedle'"
                ).fetchone()
            )
        finally:
            connection.close()

        self.write("wiki/concepts/refreshed.md", "# refreshneedle\n\nnew corpus term\n")
        self.assertTrue(wiki_search.index_is_stale(self.root))
        response = self.search("refreshneedlf")
        self.assertTrue(response.fuzzy)
        self.assertEqual(response.effective_query, "refreshneedle")

    def test_fuzzy_ordering_is_deterministic_across_runs(self) -> None:
        self.write("wiki/concepts/fuzzy-b.md", "# Fuzzy B\n\ndeterministicneedle\n")
        self.write("wiki/concepts/fuzzy-a.md", "# Fuzzy A\n\ndeterministicneedle\n")
        first = self.search("deterministicneedlf", rebuild=True)
        second = self.search("deterministicneedlf")
        self.assertEqual(first, second)
        self.assertEqual(
            [result["path"] for result in first.results],
            ["wiki/concepts/fuzzy-a.md", "wiki/concepts/fuzzy-b.md"],
        )

    def test_rebuild_only_json(self) -> None:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = search_wiki.main(["--rebuild", "--json"], root=self.root)
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(output.getvalue())["rebuilt"], ".cache/wiki-search.sqlite3")

    def test_fts5_unavailable_has_useful_error(self) -> None:
        with mock.patch.object(wiki_search.sqlite3, "connect", side_effect=sqlite3.OperationalError("no fts5")):
            with self.assertRaisesRegex(wiki_search.SearchError, "SQLite FTS5 support is required"):
                wiki_search.ensure_fts5()


if __name__ == "__main__":
    unittest.main()
