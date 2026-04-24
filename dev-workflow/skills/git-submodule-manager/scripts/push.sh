#!/bin/bash
set -e

# 사용법: ./push.sh [--force] [--yes]

source "$(dirname "$0")/_config.sh"

# --force 및 --yes 플래그 파싱
FORCE_FLAG=""
parse_yes_flag "$@"
for arg in "$@"; do
    if [ "$arg" = "--force" ]; then
        FORCE_FLAG="--force"
    fi
done

# 푸시할 항목 수집
declare -A TO_PUSH

for sub in "${SUBMODULES[@]}"; do
    if [ -d "$sub" ]; then
        branch=$(git -C "$sub" branch --show-current 2>/dev/null)
        if [ -n "$branch" ]; then
            ahead=$(git -C "$sub" rev-list --count @{u}..HEAD 2>/dev/null || echo "new")
            if [ "$ahead" != "0" ]; then
                TO_PUSH[$sub]="$branch (↑$ahead)"
            fi
        fi
    fi
done

MAIN_BRANCH=$(git branch --show-current)
MAIN_AHEAD=$(git rev-list --count @{u}..HEAD 2>/dev/null || echo "new")
if [ "$MAIN_AHEAD" != "0" ]; then
    TO_PUSH["main"]="$MAIN_BRANCH (↑$MAIN_AHEAD)"
fi

# 푸시할 내용 출력
if [ ${#TO_PUSH[@]} -eq 0 ]; then
    log_success "Everything is up to date. Nothing to push."
    exit 0
fi

echo -e "${BOLD}=== Branches to Push ===${NC}"
echo ""
for repo in "${!TO_PUSH[@]}"; do
    echo "  $repo: ${TO_PUSH[$repo]}"
done
echo ""

# 사용자 확인
confirm_action "Proceed with push?" || exit 0

# 서브모듈 먼저 푸시 (의존성 때문)
for sub in "${SUBMODULES[@]}"; do
    if [ -n "${TO_PUSH[$sub]}" ]; then
        log_info "Pushing $sub..."
        branch=$(git -C "$sub" branch --show-current)

        if [ -n "$FORCE_FLAG" ]; then
            git -C "$sub" push -u origin "$branch" --force
        else
            git -C "$sub" push -u origin "$branch"
        fi

        log_success "$sub pushed"
    fi
done

# 메인 리포지토리 푸시
if [ -n "${TO_PUSH[main]}" ]; then
    log_info "Pushing main repository..."

    if [ -n "$FORCE_FLAG" ]; then
        git push -u origin "$MAIN_BRANCH" --force
    else
        git push -u origin "$MAIN_BRANCH"
    fi

    log_success "Main repository pushed"
fi

log_success "All pushes completed!"
