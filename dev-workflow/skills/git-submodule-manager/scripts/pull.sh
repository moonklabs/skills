#!/bin/bash
set -e

# Usage: ./pull.sh [branch-name] [--yes]
# Example: ./pull.sh develop --yes
# If no branch is given, pull each repo's current branch.

source "$(dirname "$0")/_config.sh"

BRANCH_NAME=""
for arg in "$@"; do
    case "$arg" in
        --yes|-y) ;;
        --*) ;;
        *) [ -z "$BRANCH_NAME" ] && BRANCH_NAME="$arg" ;;
    esac
done

# Parse --yes flag
parse_yes_flag "$@"

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
    log_error "Please commit or stash changes before pulling"
    exit 1
fi

# Resolve target branch per repo
resolve_branch() {
    local path=$1
    if [ -n "$BRANCH_NAME" ]; then
        echo "$BRANCH_NAME"
    else
        git -C "$path" branch --show-current 2>/dev/null
    fi
}

# Show pull plan
echo ""
echo -e "${BOLD}=== Pull Plan ===${NC}"
MAIN_TARGET=$(resolve_branch ".")
if [ -z "$MAIN_TARGET" ]; then
    log_error "Main repo is in DETACHED HEAD and no branch was provided"
    exit 1
fi
echo "  Main: $MAIN_TARGET"
for sub in "${SUBMODULES[@]}"; do
    if [ -d "$sub" ]; then
        SUB_TARGET=$(resolve_branch "$sub")
        if [ -z "$SUB_TARGET" ]; then
            echo "  $sub: (skip — detached HEAD)"
        else
            echo "  $sub: $SUB_TARGET"
        fi
    fi
done
echo ""

confirm_action "Proceed with pull?" || exit 0

# Pull a single repo: fetch, checkout if needed, fast-forward
pull_repo() {
    local path=$1
    local name=$2
    local target=$3

    if [ -z "$target" ]; then
        log_warn "$name: skipping (no branch)"
        return 0
    fi

    log_info "Pulling $name ($target)..."
    git -C "$path" fetch origin

    # Switch if target differs from current
    local current
    current=$(git -C "$path" branch --show-current 2>/dev/null)
    if [ -n "$BRANCH_NAME" ] && [ "$current" != "$target" ]; then
        if git -C "$path" show-ref --verify --quiet "refs/heads/$target" || \
           git -C "$path" show-ref --verify --quiet "refs/remotes/origin/$target"; then
            git -C "$path" checkout "$target"
        else
            log_warn "$name: branch $target not found, skipping"
            return 0
        fi
    fi

    if git -C "$path" pull --ff-only origin "$target"; then
        log_success "$name pulled"
    else
        log_error "$name: pull failed (non-fast-forward or conflict)"
        return 1
    fi
}

# Pull main repo first so submodule pointers are current
pull_repo "." "main repo" "$MAIN_TARGET"

# Pull each submodule on its target branch
for sub in "${SUBMODULES[@]}"; do
    if [ -d "$sub" ]; then
        SUB_TARGET=$(resolve_branch "$sub")
        pull_repo "$sub" "$sub" "$SUB_TARGET"
    fi
done

log_success "All pulls completed!"
echo ""
echo "=== Status ==="
echo "Main: $(git branch --show-current)"
for sub in "${SUBMODULES[@]}"; do
    echo "$sub: $(git -C "$sub" branch --show-current 2>/dev/null || echo 'not initialized')"
done
