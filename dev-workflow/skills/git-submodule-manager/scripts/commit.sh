#!/bin/bash
set -e

# 사용법: ./commit.sh "commit message" [--yes]

source "$(dirname "$0")/_config.sh"

COMMIT_MSG=$1

# --yes 플래그 파싱
parse_yes_flag "$@"

# 인자 검증
if [ -z "$COMMIT_MSG" ]; then
    log_error "Commit message is required"
    echo "Usage: $0 \"commit message\" [--yes]"
    exit 1
fi

# 변경사항 수집
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

# 변경사항 출력
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

# 사용자 확인
echo ""
echo -e "Commit message: ${YELLOW}$COMMIT_MSG${NC}"
echo ""

confirm_action "Proceed with commit?" || exit 0

# 서브모듈 먼저 커밋
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

# 메인 리포지토리 커밋 (서브모듈 참조 포함)
log_info "Committing main repository..."

# 서브모듈 참조 업데이트를 위해 add
for sub in "${COMMITTED_SUBS[@]}"; do
    git add "$sub"
done

# 메인의 다른 변경사항도 add
if [ -n "$MAIN_STATUS" ]; then
    git add -A
fi

# 커밋할 내용이 있는지 확인
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
