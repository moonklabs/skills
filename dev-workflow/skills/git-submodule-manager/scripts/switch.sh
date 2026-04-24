#!/bin/bash
set -e

# Usage: ./switch.sh <branch-name> [--create] [--yes]
# Example: ./switch.sh feature/new-feature --create --yes

source "$(dirname "$0")/_config.sh"

BRANCH_NAME=$1
CREATE_FLAG=""

# Parse --create and --yes flags
parse_yes_flag "$@"
for arg in "$@"; do
    if [ "$arg" = "--create" ]; then
        CREATE_FLAG="--create"
    fi
done

# Validate arguments
if [ -z "$BRANCH_NAME" ]; then
    log_error "Branch name is required"
    echo "Usage: $0 <branch-name> [--create] [--yes]"
    echo "Example: $0 feature/new-feature --create"
    exit 1
fi

# Uncommitted-change check
check_uncommitted_changes() {
    local path=$1
    local name=$2

    if [ -n "$(git -C "$path" status --porcelain 2>/dev/null)" ]; then
        log_error "Uncommitted changes in $name"
        return 1
    fi
    return 0
}

# Run the check across every repo
log_info "Checking for uncommitted changes..."
HAS_CHANGES=false

if ! check_uncommitted_changes "." "main repo"; then
    HAS_CHANGES=true
fi

for sub in "${SUBMODULES[@]}"; do
    if [ -d "$sub" ] && ! check_uncommitted_changes "$sub" "$sub"; then
        HAS_CHANGES=true
    fi
done

if [ "$HAS_CHANGES" = true ]; then
    log_error "Please commit or stash changes before switching branches"
    exit 1
fi

# Current state
log_info "Current branches:"
echo "  Main: $(git branch --show-current)"
for sub in "${SUBMODULES[@]}"; do
    echo "  $sub: $(git -C $sub branch --show-current 2>/dev/null || echo 'not initialized')"
done

# Switch / create branch
echo ""
log_info "Switching to: $BRANCH_NAME"

# 1. Main repo
if [ "$CREATE_FLAG" = "--create" ]; then
    log_info "Creating and switching main repo branch..."
    git checkout -B "$BRANCH_NAME"
else
    log_info "Switching main repo branch..."
    git checkout "$BRANCH_NAME"
fi

# 2. Submodules
for sub in "${SUBMODULES[@]}"; do
    if [ ! -d "$sub/.git" ] && [ ! -f "$sub/.git" ]; then
        log_warn "$sub is not initialized, skipping"
        continue
    fi

    log_info "Processing $sub..."
    cd "$sub"
    git fetch origin

    if [ "$CREATE_FLAG" = "--create" ]; then
        DEFAULT_BRANCH=$(get_default_branch "$sub")
        if git show-ref --verify --quiet "refs/remotes/origin/$BRANCH_NAME"; then
            git checkout -B "$BRANCH_NAME" "origin/$BRANCH_NAME"
        else
            git checkout -B "$BRANCH_NAME" "origin/$DEFAULT_BRANCH"
        fi
    else
        if git show-ref --verify --quiet "refs/heads/$BRANCH_NAME" || \
           git show-ref --verify --quiet "refs/remotes/origin/$BRANCH_NAME"; then
            git checkout "$BRANCH_NAME"
        else
            log_warn "Branch $BRANCH_NAME not found in $sub, keeping current branch"
        fi
    fi

    cd ..
done

# Final state
log_success "Branch switch completed!"
echo ""
echo "=== New Status ==="
echo "Main: $(git branch --show-current)"
for sub in "${SUBMODULES[@]}"; do
    echo "$sub: $(git -C $sub branch --show-current 2>/dev/null || echo 'not initialized')"
done
