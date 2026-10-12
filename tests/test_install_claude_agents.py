#!/usr/bin/env python3
"""Tests for linking ~/.claude/agents to the repository's agent definitions."""

from __future__ import annotations

import sys
import tempfile
import unittest
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "claude-config"))

from install_claude_agents import InstallError, link_agents  # noqa: E402

NOW = datetime(2026, 10, 12, 9, 30, 0)


class LinkAgentsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        root = Path(self.temporary.name)
        self.repo = root / "repo" / "agents"
        self.repo.mkdir(parents=True)
        (self.repo / "scout.md").write_text("scout\n")
        self.target = root / "home" / ".claude" / "agents"

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_fresh_machine_gets_a_link(self) -> None:
        link_agents(self.repo, self.target)
        self.assertTrue(self.target.is_symlink())
        self.assertEqual((self.target / "scout.md").read_text(), "scout\n")

    def test_existing_directory_is_backed_up_and_unmerged_files_reported(self) -> None:
        self.target.mkdir(parents=True)
        (self.target / "scout.md").write_text("scout\n")
        (self.target / "local-only.md").write_text("mine\n")
        actions = link_agents(self.repo, self.target, now=NOW)
        backup = self.target.with_name("agents.backup-20261012-093000")
        self.assertEqual((backup / "local-only.md").read_text(), "mine\n")
        self.assertTrue(self.target.is_symlink())
        self.assertTrue(any("local-only.md" in action for action in actions))
        self.assertFalse(any("scout.md" in action for action in actions))

    def test_dry_run_and_rerun_change_nothing(self) -> None:
        self.target.mkdir(parents=True)
        link_agents(self.repo, self.target, dry_run=True)
        self.assertFalse(self.target.is_symlink())
        self.target.rmdir()
        link_agents(self.repo, self.target)
        self.assertIn("already links", link_agents(self.repo, self.target)[0])

    def test_foreign_symlink_is_refused(self) -> None:
        other = self.repo.parent / "other"
        other.mkdir()
        self.target.parent.mkdir(parents=True)
        self.target.symlink_to(other)
        with self.assertRaises(InstallError):
            link_agents(self.repo, self.target)


if __name__ == "__main__":
    unittest.main()
