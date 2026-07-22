# git-submodule-manager

A Claude Code skill that unifies Git worktree + submodule management for any monorepo that uses git submodules.

## Overview

Manages the worktree lifecycle for a monorepo with git submodules. The submodule list and their default branches are auto-detected from `.gitmodules` at runtime (see [Submodule Discovery](#submodule-discovery) below) — nothing is hardcoded per project, so the same scripts work unmodified across repos.

## Installation

This skill ships as part of the `moonklabs-dev-workflow` plugin in the [moonklabs/skills](https://github.com/moonklabs/skills) marketplace.

```bash
# 1. Register the marketplace (path to your local clone of moonklabs/skills)
/plugin marketplace add /path/to/skills

# 2. Install the plugin
/plugin install moonklabs-dev-workflow@moonklabs-skills-marketplace

# 3. Restart Claude Code, then use
```

## Commands

| Command | Description | Arguments |
|---------|-------------|-----------|
| `/git-submodule-manager:create` | Create a new feature worktree | `<feature-name> [base-branch]` |
| `/git-submodule-manager:status` | Show full worktree/submodule status | — |
| `/git-submodule-manager:commit` | Unified commit across submodules + main | `[commit message]` |
| `/git-submodule-manager:push` | Unified push of submodules + main | `[--force]` |
| `/git-submodule-manager:pull` | Fast-forward pull across submodules + main | `[branch-name]` |
| `/git-submodule-manager:switch` | Switch branches across submodules + main | `<branch-name> [--create]` |

## Skill Auto-Trigger

The `git-submodule-manager` skill activates automatically on the following phrases:
- "create a worktree", "new feature branch", "worktree 만들어줘", "새 feature 브랜치"
- "worktree status", "check branches", "상태 확인", "브랜치 확인"
- "commit", "commit changes", "커밋해줘", "변경사항 커밋"
- "push", "push to remote", "푸시해줘", "원격에 올려줘"
- "pull", "pull latest", "sync from remote", "풀받아줘", "최신 받아줘"
- "switch branch", "checkout", "브랜치 전환", "브랜치 바꿔줘"

## Architecture

This skill lives inside the `dev-workflow` category plugin of the `moonklabs/skills` marketplace:

```
skills/                              # marketplace repo root
├── .claude-plugin/marketplace.json  # registers moonklabs-dev-workflow + 5 other plugins
└── dev-workflow/
    ├── .claude-plugin/plugin.json   # moonklabs-dev-workflow plugin metadata
    └── skills/git-submodule-manager/
        ├── SKILL.md                 # dispatcher skill definition
        ├── README.md                # this file
        ├── scripts/
        │   ├── _config.sh           # submodule auto-discovery, colors, logging, flag parsing
        │   ├── create.sh            # create worktree
        │   ├── status.sh            # show status
        │   ├── commit.sh            # unified commit
        │   ├── push.sh              # unified push
        │   ├── pull.sh              # unified pull
        │   └── switch.sh            # branch switching
        ├── references/
        │   └── submodule-map.md     # how default-branch resolution works
        └── commands/                # slash commands (thin wrappers)
            ├── create.md
            ├── status.md
            ├── commit.md
            ├── push.md
            ├── pull.md
            └── switch.md
```

## Submodule Discovery

No submodule list or branch mapping is hardcoded. Every script sources `_config.sh`, which:

1. Reads submodule paths straight from `.gitmodules`
2. Resolves each submodule's default branch from `.gitmodules`' own `branch = ...` field (set via `git submodule set-branch --branch <branch> <path>`), falling back to the submodule's remote HEAD if no override is set

If a submodule in your repo should track a non-default branch, set it once with `git submodule set-branch` and commit the `.gitmodules` change — every script picks it up automatically.

## Running Scripts Directly

```bash
# Show status (compact — recommended default)
bash skills/git-submodule-manager/scripts/status.sh --quiet

# Create worktree (non-interactive)
bash skills/git-submodule-manager/scripts/create.sh my-feature main --yes

# Unified commit (non-interactive, compact)
bash skills/git-submodule-manager/scripts/commit.sh "feat: add feature" --yes --quiet

# Unified push (non-interactive, compact)
bash skills/git-submodule-manager/scripts/push.sh --yes --quiet

# Branch switch
bash skills/git-submodule-manager/scripts/switch.sh feature/my-feature --yes
```

Flags:
- `--yes` / `-y`: auto-approves every confirmation prompt (required when Claude invokes scripts non-interactively)
- `--quiet` / `-q`: collapses output to one line per repo instead of a full box/diff dump — use it for routine checks to keep tool-output tokens small; drop it when you actually need file-level detail
