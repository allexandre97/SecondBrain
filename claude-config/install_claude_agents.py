#!/usr/bin/env python3
"""Link ~/.claude/agents to the agent definitions kept in this repository.

Run once per machine from any directory:

    python3 claude-config/install_claude_agents.py --dry-run
    python3 claude-config/install_claude_agents.py

An existing ~/.claude/agents directory is never deleted: it is renamed to
~/.claude/agents.backup-<timestamp>, and any of its files that are missing
from or differ from the repository copy are listed so they can be merged.
"""

from __future__ import annotations

import argparse
import filecmp
import sys
from datetime import datetime
from pathlib import Path
from typing import Sequence


REPO_AGENTS = Path(__file__).resolve().parent / "agents"
DEFAULT_TARGET = Path.home() / ".claude" / "agents"


class InstallError(RuntimeError):
    pass


def unmerged_files(existing: Path, repo_agents: Path) -> list[str]:
    """Files in the existing directory that the repository copy lacks or differs from."""
    return sorted(
        path.name
        for path in existing.iterdir()
        if path.is_file()
        and not ((repo_agents / path.name).is_file() and filecmp.cmp(path, repo_agents / path.name, shallow=False))
    )


def link_agents(repo_agents: Path, target: Path, *, dry_run: bool = False, now: datetime | None = None) -> list[str]:
    """Point target at repo_agents; return human-readable actions taken (or planned)."""
    repo_agents = repo_agents.resolve()
    if not repo_agents.is_dir():
        raise InstallError(f"repository agent directory not found: {repo_agents}")
    if target.is_symlink():
        if target.resolve() == repo_agents:
            return [f"{target} already links to {repo_agents}"]
        raise InstallError(f"{target} is a symlink to {target.resolve()}; remove it manually first")

    actions = []
    if target.exists():
        if not target.is_dir():
            raise InstallError(f"{target} exists and is not a directory")
        stamp = (now or datetime.now()).strftime("%Y%m%d-%H%M%S")
        backup = target.with_name(f"{target.name}.backup-{stamp}")
        if backup.exists():
            raise InstallError(f"backup path already exists: {backup}")
        for name in unmerged_files(target, repo_agents):
            actions.append(f"NOT IN REPOSITORY (merge by hand from the backup): {name}")
        actions.append(f"rename {target} -> {backup}")
        if not dry_run:
            target.rename(backup)
    actions.append(f"link {target} -> {repo_agents}")
    if not dry_run:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.symlink_to(repo_agents, target_is_directory=True)
    return actions


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true", help="Show what would happen without changing anything.")
    args = parser.parse_args(argv)
    try:
        actions = link_agents(REPO_AGENTS, DEFAULT_TARGET, dry_run=args.dry_run)
    except InstallError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    prefix = "Would " if args.dry_run else ""
    for action in actions:
        print(f"{prefix}{action}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
