# Submodule Branch Mapping

## Submodules

| Path | Repository | Default Branch | Purpose |
|------|------------|----------------|---------|
| `admin-backend` | moonklabs/sellerking-admin-backend | `develop-ai` | NestJS admin API |
| `backend` | moonklabs/sellerking-backend | `develop` | NestJS main API |
| `batch` | moonklabs/sellerking-scraper | `develop` | Scraping batch jobs |

## Branching Strategy

### Feature Branches
- Format: `feature/{feature-name}`
- Examples: `feature/batch-queue-prd`, `feature/user-auth`
- Created on main and every submodule with the same name

### Per-Submodule Default Branch (base when no feature branch exists yet)
- `admin-backend`: `develop-ai` — AI feature development
- `backend`: `develop` — main API development
- `batch`: `develop` — batch/scraper development

### Branch Creation Rules
1. If the remote already has the feature branch → check it out from the remote
2. Otherwise → create a new branch from the submodule's default branch

## Worktree Path Convention

```
../sellerking-data-monolith-{feature-name}/
├── admin-backend/      # Submodule (feature branch)
├── backend/            # Submodule (feature branch)
├── batch/              # Submodule (feature branch)
└── ...                 # Main repo files
```

## Commit/Push Order

To keep submodule pointers consistent, always process in this order:

1. `admin-backend` (if it has changes)
2. `backend` (if it has changes)
3. `batch` (if it has changes)
4. `main` — submodule pointer updates (`.gitmodules` + commits) plus any main-only changes

## Cautions

- Submodules are pinned to specific commit SHAs → always update the main repo's pointer after a submodule commit
- Always run `git checkout {branch}` on each submodule before working (prevents detached HEAD)
- Run `git submodule update --init --recursive` from the monorepo root to initialize fresh clones
