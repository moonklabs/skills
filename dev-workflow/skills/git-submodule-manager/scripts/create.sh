#!/bin/bash
set -e

# Usage: ./create.sh <feature-name> [base-branch] [--yes]
# Example: ./create.sh batch-queue-prd main --yes

source "$(dirname "$0")/_config.sh"

FEATURE_NAME=$1
BASE_BRANCH=${2:-main}

# Parse --yes flag
parse_yes_flag "$@"

# Validate arguments
if [ -z "$FEATURE_NAME" ]; then
    log_error "Feature name is required"
    echo "Usage: $0 <feature-name> [base-branch] [--yes]"
    echo "Example: $0 batch-queue-prd main"
    exit 1
fi

# Worktree path
WORKTREE_PATH="../sellerking-data-monolith-${FEATURE_NAME}"
FEATURE_BRANCH="feature/${FEATURE_NAME}"

# 1. Guard against existing worktree
if git worktree list | grep -q "$WORKTREE_PATH"; then
    log_error "Worktree already exists at: $WORKTREE_PATH"
    exit 1
fi

log_info "Creating worktree for feature: ${FEATURE_NAME}"

# 2. Show plan and confirm
echo ""
echo "Will create:"
echo "  - Worktree path: $WORKTREE_PATH"
echo "  - Main branch: $FEATURE_BRANCH (from $BASE_BRANCH)"
echo "  - Submodule branches:"
for sub in "${SUBMODULES[@]}"; do
    echo "    - $sub: $FEATURE_BRANCH (from $(get_default_branch "$sub"))"
done
echo ""

confirm_action "Continue?" || exit 0

# 3. Create feature branch on main repo and add worktree
log_info "Creating main worktree..."
git fetch origin
git branch "$FEATURE_BRANCH" "origin/$BASE_BRANCH" 2>/dev/null || log_warn "Branch $FEATURE_BRANCH may already exist"
git worktree add "$WORKTREE_PATH" "$FEATURE_BRANCH"

# 4. Initialize submodules
log_info "Initializing submodules..."
cd "$WORKTREE_PATH"
git submodule init
git submodule update --recursive

# 5. Create feature branch on each submodule
log_info "Setting up submodule branches..."
for sub in "${SUBMODULES[@]}"; do
    log_info "  Processing $sub..."
    cd "$WORKTREE_PATH/$sub"

    # Fetch remote
    git fetch origin

    # Create feature branch from the default branch
    DEFAULT_BRANCH=$(get_default_branch "$sub")
    if git show-ref --verify --quiet "refs/remotes/origin/$FEATURE_BRANCH"; then
        # Feature branch already exists on remote — check it out
        git checkout -B "$FEATURE_BRANCH" "origin/$FEATURE_BRANCH"
        log_info "    Checked out existing remote branch"
    else
        # Otherwise create from default branch
        git checkout -B "$FEATURE_BRANCH" "origin/$DEFAULT_BRANCH"
        log_info "    Created new branch from $DEFAULT_BRANCH"
    fi
done

cd "$WORKTREE_PATH"

# 6. Print final status
log_success "Worktree created successfully!"
echo ""
echo "=== Status ==="
echo "Main repo: $(git branch --show-current)"
for sub in "${SUBMODULES[@]}"; do
    echo "$sub: $(git -C $sub branch --show-current)"
done
echo ""
echo "To start working:"
echo "  cd $WORKTREE_PATH"
