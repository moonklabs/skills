# Submodule Branch Resolution

This skill has no repo-specific submodule list or branch table baked in. `_config.sh` derives everything from `.gitmodules` at runtime, so this reference describes the *mechanism*, not a fixed mapping — read your own repo's `.gitmodules` for the actual list.

## Where the submodule list comes from

```bash
git config --file .gitmodules --get-regexp path
```

Every path returned becomes an entry in `SUBMODULES` — add or remove a submodule with normal `git submodule add`/`deinit` and the scripts follow automatically.

## Where each submodule's default branch comes from

Resolution order, first match wins:

1. **`.gitmodules` `branch =` field** — the git-native way to pin a submodule to a specific branch:
   ```bash
   git submodule set-branch --branch develop-ai admin-backend
   git add .gitmodules && git commit -m "chore: pin admin-backend to develop-ai"
   ```
2. **The submodule's remote HEAD** (`origin/HEAD`), if no override is set — read locally first, falling back to a live `git remote show origin` query only when the local ref is missing

Use step 1 whenever a submodule's default branch differs from its own repo's `HEAD` (e.g. an AI-focused fork that develops off `develop-ai` instead of `develop`) — everything else needs no configuration at all.

## Branching Strategy

### Feature Branches
- Format: `feature/{feature-name}`
- Created on main and every detected submodule with the same name

### Branch Creation Rules
1. If the remote already has the feature branch → check it out from the remote
2. Otherwise → create a new branch from the submodule's resolved default branch (see above)

## Worktree Path Convention

The worktree directory name is derived from the main repo's own directory name, not hardcoded:

```
../{repo-name}-{feature-name}/
├── {submodule-1}/      # Submodule (feature branch)
├── {submodule-2}/      # Submodule (feature branch)
└── ...                 # Main repo files
```

## Commit/Push Order

To keep submodule pointers consistent, always process in this order:

1. Each submodule with changes, in the order `.gitmodules` lists them
2. `main` — submodule pointer updates (`.gitmodules` + commits) plus any main-only changes

## Cautions

- Submodules are pinned to specific commit SHAs → always update the main repo's pointer after a submodule commit
- Always run `git checkout {branch}` on each submodule before working (prevents detached HEAD)
- Run `git submodule update --init --recursive` from the monorepo root to initialize fresh clones
