#!/bin/bash
set -e

# Usage: ./push.sh [--force] [--yes]

source "$(dirname "$0")/_config.sh"

# Parse --force, --yes and --quiet flags
FORCE_FLAG=""
parse_yes_flag "$@"
parse_quiet_flag "$@"
for arg in "$@"; do
    if [ "$arg" = "--force" ]; then
        FORCE_FLAG="--force"
    fi
done

# Collect push targets. Uses parallel indexed arrays (not `declare -A`):
# macOS's default /bin/bash (3.2) doesn't support associative arrays, and
# under `set -e` that failure would abort this whole script before it runs.
PUSH_SUBS=()
PUSH_DESCS=()

for sub in "${SUBMODULES[@]}"; do
    if [ -d "$sub" ]; then
        branch=$(git -C "$sub" branch --show-current 2>/dev/null)
        if [ -n "$branch" ]; then
            ahead=$(git -C "$sub" rev-list --count @{u}..HEAD 2>/dev/null || echo "new")
            if [ "$ahead" != "0" ]; then
                PUSH_SUBS+=("$sub")
                PUSH_DESCS+=("$branch (↑$ahead)")
            fi
        fi
    fi
done

MAIN_BRANCH=$(git branch --show-current)
MAIN_AHEAD=$(git rev-list --count @{u}..HEAD 2>/dev/null || echo "new")
MAIN_TO_PUSH=false
if [ "$MAIN_AHEAD" != "0" ]; then
    MAIN_TO_PUSH=true
fi

# Print push targets
if [ ${#PUSH_SUBS[@]} -eq 0 ] && [ "$MAIN_TO_PUSH" = "false" ]; then
    log_success "Everything is up to date. Nothing to push."
    exit 0
fi

if [ "$QUIET_FLAG" != "true" ]; then
    echo -e "${BOLD}=== Branches to Push ===${NC}"
    echo ""
fi
for i in "${!PUSH_SUBS[@]}"; do
    echo "  ${PUSH_SUBS[$i]}: ${PUSH_DESCS[$i]}"
done
[ "$MAIN_TO_PUSH" = "true" ] && echo "  main: $MAIN_BRANCH (↑$MAIN_AHEAD)"
[ "$QUIET_FLAG" != "true" ] && echo ""

# Confirm
confirm_action "Proceed with push?" || exit 0

# Push submodules first (pointer dependency on main)
for sub in "${PUSH_SUBS[@]}"; do
    log_info "Pushing $sub..."
    branch=$(git -C "$sub" branch --show-current)

    if [ -n "$FORCE_FLAG" ]; then
        git -C "$sub" push -u origin "$branch" --force
    else
        git -C "$sub" push -u origin "$branch"
    fi

    log_success "$sub pushed"
done

# Push main repo
if [ "$MAIN_TO_PUSH" = "true" ]; then
    log_info "Pushing main repository..."

    if [ -n "$FORCE_FLAG" ]; then
        git push -u origin "$MAIN_BRANCH" --force
    else
        git push -u origin "$MAIN_BRANCH"
    fi

    log_success "Main repository pushed"
fi

log_success "All pushes completed!"
