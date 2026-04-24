#!/bin/bash
set -e

# Usage: ./commit.sh "commit message" [--yes]

source "$(dirname "$0")/_config.sh"

COMMIT_MSG=$1

# Parse --yes flag
parse_yes_flag "$@"

# Validate arguments
if [ -z "$COMMIT_MSG" ]; then
    log_error "Commit message is required"
    echo "Usage: $0 \"commit message\" [--yes]"
    exit 1
fi

# Collect changes
declare -A CHANGES

for sub in "${SUBMODULES[@]}"; do
    if [ -d "$sub" ]; then
        status=$(git -C "$sub" status --porcelain 2>/dev/null)
        if [ -n "$status" ]; then
            CHANGES[$sub]="$status"
        fi
    fi
done

MAIN_STATUS=$(git status --porcelain 2>/dev/null | grep -v "^?? " | grep -v "admin-backend" | grep -v "backend" | grep -v "batch")

# Print changes
echo -e "${BOLD}=== Changes to Commit ===${NC}"
echo ""

TOTAL_CHANGES=0

for sub in "${!CHANGES[@]}"; do
    echo -e "${BLUE}$sub:${NC}"
    echo "${CHANGES[$sub]}" | head -10
    count=$(echo "${CHANGES[$sub]}" | wc -l | tr -d ' ')
    if [ "$count" -gt 10 ]; then
        echo "  ... and $((count - 10)) more files"
    fi
    TOTAL_CHANGES=$((TOTAL_CHANGES + 1))
    echo ""
done

if [ -n "$MAIN_STATUS" ]; then
    echo -e "${BLUE}Main repository:${NC}"
    echo "$MAIN_STATUS" | head -10
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
for sub in "${SUBMODULES[@]}"; do
    if [ -n "${CHANGES[$sub]}" ]; then
        log_info "Committing $sub..."
        cd "$sub"
        git add -A
        git commit -m "$COMMIT_MSG"
        cd ..
        COMMITTED_SUBS+=("$sub")
        log_success "$sub committed"
    fi
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
