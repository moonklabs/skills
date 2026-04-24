#!/bin/bash

source "$(dirname "$0")/_config.sh"

echo -e "${BOLD}${CYAN}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BOLD}${CYAN}║           Worktree & Submodule Status                        ║${NC}"
echo -e "${BOLD}${CYAN}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""

# 현재 디렉토리
echo -e "${BOLD}📍 Current Directory:${NC} $(pwd)"
echo ""

# Worktree 목록
echo -e "${BOLD}🌳 Git Worktrees:${NC}"
git worktree list | while read line; do
    echo "   $line"
done
echo ""

# 상태 출력 함수
show_repo_status() {
    local name=$1
    local path=$2
    local default_branch=$3

    if [ ! -d "$path" ] || ([ ! -f "$path/.git" ] && [ ! -d "$path/.git" ]); then
        echo -e "│ ${YELLOW}⚠${NC}  ${BOLD}$name${NC}: Not initialized"
        return
    fi

    local current_branch=$(git -C "$path" branch --show-current 2>/dev/null)
    if [ -z "$current_branch" ]; then
        current_branch="DETACHED HEAD"
    fi

    local status=$(git -C "$path" status --porcelain 2>/dev/null)
    local staged=$(echo "$status" | grep "^[MADRC]" | wc -l | tr -d ' ')
    local unstaged=$(echo "$status" | grep "^.[MADRC]" | wc -l | tr -d ' ')
    local untracked=$(echo "$status" | grep "^??" | wc -l | tr -d ' ')

    # 브랜치 색상
    local branch_color=$GREEN
    if [ "$current_branch" = "DETACHED HEAD" ]; then
        branch_color=$RED
    elif [[ "$current_branch" == feature/* ]]; then
        branch_color=$CYAN
    fi

    # 상태 아이콘
    local status_icon="${GREEN}✓${NC}"
    if [ -n "$status" ]; then
        status_icon="${YELLOW}●${NC}"
    fi

    echo -e "│ $status_icon ${BOLD}$name${NC}"
    echo -e "│   Branch: ${branch_color}$current_branch${NC}"
    [ -n "$default_branch" ] && echo -e "│   Default: $default_branch"

    if [ -n "$status" ]; then
        echo -e "│   Changes: ${GREEN}+$staged staged${NC}, ${YELLOW}~$unstaged modified${NC}, ${RED}?$untracked untracked${NC}"
    fi

    # 원격과의 차이
    local ahead=$(git -C "$path" rev-list --count @{u}..HEAD 2>/dev/null || echo "0")
    local behind=$(git -C "$path" rev-list --count HEAD..@{u} 2>/dev/null || echo "0")
    if [ "$ahead" != "0" ] || [ "$behind" != "0" ]; then
        echo -e "│   Remote: ↑$ahead ↓$behind"
    fi
}

# 메인 리포지토리
echo -e "${BOLD}📦 Repository Status:${NC}"
echo "├──────────────────────────────────────────────────────────────"
show_repo_status "Main Repository" "." ""
echo "│"

# 서브모듈
for sub in "${SUBMODULES[@]}"; do
    show_repo_status "$sub" "$sub" "$(get_default_branch "$sub")"
    echo "│"
done
echo "└──────────────────────────────────────────────────────────────"

# 경고 메시지
echo ""
WARNINGS=()

# Detached HEAD 체크
for sub in "${SUBMODULES[@]}"; do
    if [ -d "$sub" ]; then
        branch=$(git -C "$sub" branch --show-current 2>/dev/null)
        if [ -z "$branch" ]; then
            WARNINGS+=("$sub is in DETACHED HEAD state")
        fi
    fi
done

# 브랜치 불일치 체크
MAIN_BRANCH=$(git branch --show-current)
for sub in "${SUBMODULES[@]}"; do
    if [ -d "$sub" ]; then
        SUB_BRANCH=$(git -C "$sub" branch --show-current 2>/dev/null)
        if [[ "$MAIN_BRANCH" == feature/* ]] && [ "$SUB_BRANCH" != "$MAIN_BRANCH" ]; then
            WARNINGS+=("$sub branch ($SUB_BRANCH) differs from main ($MAIN_BRANCH)")
        fi
    fi
done

if [ ${#WARNINGS[@]} -gt 0 ]; then
    echo -e "${YELLOW}${BOLD}⚠ Warnings:${NC}"
    for warn in "${WARNINGS[@]}"; do
        echo -e "  ${YELLOW}•${NC} $warn"
    done
fi
