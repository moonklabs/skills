#!/bin/bash
set -e

# 사용법: ./switch.sh <branch-name> [--create] [--yes]
# 예: ./switch.sh feature/new-feature --create --yes

source "$(dirname "$0")/_config.sh"

BRANCH_NAME=$1
CREATE_FLAG=""

# --create 및 --yes 플래그 파싱
parse_yes_flag "$@"
for arg in "$@"; do
    if [ "$arg" = "--create" ]; then
        CREATE_FLAG="--create"
    fi
done

# 인자 검증
if [ -z "$BRANCH_NAME" ]; then
    log_error "Branch name is required"
    echo "Usage: $0 <branch-name> [--create] [--yes]"
    echo "Example: $0 feature/new-feature --create"
    exit 1
fi

# 변경사항 확인
check_uncommitted_changes() {
    local path=$1
    local name=$2

    if [ -n "$(git -C "$path" status --porcelain 2>/dev/null)" ]; then
        log_error "Uncommitted changes in $name"
        return 1
    fi
    return 0
}

# 변경사항 체크
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

# 현재 상태 출력
log_info "Current branches:"
echo "  Main: $(git branch --show-current)"
for sub in "${SUBMODULES[@]}"; do
    echo "  $sub: $(git -C $sub branch --show-current 2>/dev/null || echo 'not initialized')"
done

# 브랜치 전환/생성
echo ""
log_info "Switching to: $BRANCH_NAME"

# 1. 메인 리포지토리
if [ "$CREATE_FLAG" = "--create" ]; then
    log_info "Creating and switching main repo branch..."
    git checkout -B "$BRANCH_NAME"
else
    log_info "Switching main repo branch..."
    git checkout "$BRANCH_NAME"
fi

# 2. 서브모듈
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

# 최종 상태
log_success "Branch switch completed!"
echo ""
echo "=== New Status ==="
echo "Main: $(git branch --show-current)"
for sub in "${SUBMODULES[@]}"; do
    echo "$sub: $(git -C $sub branch --show-current 2>/dev/null || echo 'not initialized')"
done
