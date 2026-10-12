# Claude Code Agents

`agents/` holds the user-level Claude Code subagent definitions (`scout`, `worker`, `reviewer`, `oracle`, `secondbrain`, `blender`) shared between workstations. On each machine, `~/.claude/agents` is a symlink to this directory, so `git pull` updates the agents, and agents created or edited through Claude Code land here, ready to commit.

## Setting up a machine

```sh
python3 claude-config/install_claude_agents.py --dry-run   # preview
python3 claude-config/install_claude_agents.py
```

An existing `~/.claude/agents` directory is renamed to `~/.claude/agents.backup-<timestamp>`, never deleted. The script lists any of its files that are missing from or differ from this repository; merge those into `agents/` by hand, commit, and then delete the backup.

## What stays per machine

Only machine-independent instructions belong in `agents/`. Paths, executables, model routing overrides, and other machine-specific values belong in each machine's `~/.claude/LOCAL_ENVIRONMENT.md`, which agents are told to read. For example, the `secondbrain` agent finds this repository's path there.
