#!/bin/bash
set -e

# Usage: ./commit.sh "commit message" [--yes]

source "$(dirname "$0")/_config.sh"

COMMIT_MSG=$1

# Parse --yes / --quiet flags
parse_yes_flag "$@"
parse_quiet_flag "$@"

# Validate arguments
if [ -z "$COMMIT_MSG" ]; then
    log_error "Commit message is required"
    echo "Usage: $0 \"commit message\" [--yes]"
    exit 1
fi

# Collect changed submodules. Uses a plain indexed array (not `declare -A`):
# macOS's default /bin/bash (3.2) doesn't support associative arrays, and
# under `set -e` that failure would abort this whole script before it runs.
CHANGED_SUBS=()
for sub in "${SUBMODULES[@]}"; do
    if [ -d "$sub" ] && [ -n "$(git -C "$sub" status --porcelain 2>/dev/null)" ]; then
        CHANGED_SUBS+=("$sub")
    fi
done

# Build the submodule-path exclusion pattern dynamically instead of
# hardcoding submodule names, so main-repo status filtering works in any repo
if [ ${#SUBMODULES[@]} -gt 0 ]; then
    EXCLUDE_PATTERN=$(IFS='|'; echo "${SUBMODULES[*]}")
    MAIN_STATUS=$(git status --porcelain 2>/dev/null | grep -v "^?? " | grep -Ev "$EXCLUDE_PATTERN")
else
    MAIN_STATUS=$(git status --porcelain 2>/dev/null | grep -v "^?? ")
fi

# Print changes. --quiet prints one line per repo (file count only) instead
# of dumping every changed path — use it for routine commits to keep the
# tool output Claude reads back small.
echo -e "${BOLD}=== Changes to Commit ===${NC}"
echo ""

TOTAL_CHANGES=0

for sub in "${CHANGED_SUBS[@]}"; do
    status=$(git -C "$sub" status --porcelain 2>/dev/null)
    count=$(echo "$status" | wc -l | tr -d ' ')
    if [ "$QUIET_FLAG" = "true" ]; then
        echo -e "${BLUE}$sub:${NC} $count file(s) changed"
    else
        echo -e "${BLUE}$sub:${NC}"
        echo "$status" | head -10
        if [ "$count" -gt 10 ]; then
            echo "  ... and $((count - 10)) more files"
        fi
    fi
    TOTAL_CHANGES=$((TOTAL_CHANGES + 1))
    echo ""
done

if [ -n "$MAIN_STATUS" ]; then
    if [ "$QUIET_FLAG" = "true" ]; then
        count=$(echo "$MAIN_STATUS" | wc -l | tr -d ' ')
        echo -e "${BLUE}Main repository:${NC} $count file(s) changed"
    else
        echo -e "${BLUE}Main repository:${NC}"
        echo "$MAIN_STATUS" | head -10
    fi
    TOTAL_CHANGES=$((TOTAL_CHANGES + 1))
fi

if [ $TOTAL_CHANGES -eq 0 ]; then
    log_warn "No changes to commit"
    exit 0
fi

# Confirm with user
echo ""
echo -e "Commit message: ${YELLOW}$COMMIT_MSG${NC}"
echo ""

confirm_action "Proceed with commit?" || exit 0

# Commit submodules first
COMMITTED_SUBS=()
for sub in "${CHANGED_SUBS[@]}"; do
    log_info "Committing $sub..."
    cd "$sub"
    git add -A
    git commit -m "$COMMIT_MSG"
    cd ..
    COMMITTED_SUBS+=("$sub")
    log_success "$sub committed"
done

# Commit main repo (including submodule pointer updates)
log_info "Committing main repository..."

# Stage submodule pointer updates
for sub in "${COMMITTED_SUBS[@]}"; do
    git add "$sub"
done

# Stage any remaining main-repo changes
if [ -n "$MAIN_STATUS" ]; then
    git add -A
fi

# Skip commit if nothing is staged
if git diff --cached --quiet; then
    log_warn "No staged changes in main repository"
else
    git commit -m "$COMMIT_MSG"
    log_success "Main repository committed"
fi

log_success "All commits completed!"
echo ""
echo "=== Summary ==="
echo "Committed message: $COMMIT_MSG"
echo "Submodules: ${COMMITTED_SUBS[*]:-none}"
