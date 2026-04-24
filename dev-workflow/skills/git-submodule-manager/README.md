# git-submodule-manager

A Claude Code plugin that unifies Git worktree + submodule management for `sellerking-data-monolith`.

## Overview

Manages the worktree lifecycle for a monorepo containing three git submodules (`admin-backend`, `backend`, `batch`).

## Installation

```bash
# 1. Register the local marketplace
/plugin marketplace add /Users/drumcap/workspace/sellerking-data-monolith/git-submodule-manager

# 2. Install the plugin
/plugin install git-submodule-manager@git-submodule-manager-dev

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

```
git-submodule-manager/
├── .claude-plugin/
│   ├── plugin.json          # Plugin metadata
│   └── marketplace.json     # Local development marketplace
├── skills/
│   └── git-submodule-manager/
│       ├── SKILL.md         # Dispatcher skill definition
│       ├── scripts/
│       │   ├── _config.sh   # Shared config (submodule list, colors, utilities)
│       │   ├── create.sh    # Create worktree
│       │   ├── status.sh    # Show status
│       │   ├── commit.sh    # Unified commit
│       │   ├── push.sh      # Unified push
│       │   ├── pull.sh      # Unified pull
│       │   └── switch.sh    # Branch switching
│       └── references/
│           └── submodule-map.md  # Submodule branch mapping reference
├── commands/                # Slash commands (thin wrappers)
│   ├── create.md
│   ├── status.md
│   ├── commit.md
│   ├── push.md
│   ├── pull.md
│   └── switch.md
└── README.md
```

## Submodule Mapping

| Path | Default Branch |
|------|----------------|
| `admin-backend` | `develop-ai` |
| `backend` | `develop` |
| `batch` | `develop` |

## Running Scripts Directly

```bash
# Show status
bash skills/git-submodule-manager/scripts/status.sh

# Create worktree (non-interactive)
bash skills/git-submodule-manager/scripts/create.sh my-feature main --yes

# Unified commit (non-interactive)
bash skills/git-submodule-manager/scripts/commit.sh "feat: add feature" --yes

# Unified push (non-interactive)
bash skills/git-submodule-manager/scripts/push.sh --yes

# Branch switch
bash skills/git-submodule-manager/scripts/switch.sh feature/my-feature --yes
```

`--yes` flag: auto-approves every confirmation prompt (required when Claude invokes scripts non-interactively).
