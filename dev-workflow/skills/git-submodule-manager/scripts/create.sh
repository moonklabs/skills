#!/bin/bash
set -e

# 사용법: ./create.sh <feature-name> [base-branch] [--yes]
# 예: ./create.sh batch-queue-prd main --yes

source "$(dirname "$0")/_config.sh"

FEATURE_NAME=$1
BASE_BRANCH=${2:-main}

# --yes 플래그 파싱
parse_yes_flag "$@"

# 인자 검증
if [ -z "$FEATURE_NAME" ]; then
    log_error "Feature name is required"
    echo "Usage: $0 <feature-name> [base-branch] [--yes]"
    echo "Example: $0 batch-queue-prd main"
    exit 1
fi

# Worktree 경로 설정
WORKTREE_PATH="../sellerking-data-monolith-${FEATURE_NAME}"
FEATURE_BRANCH="feature/${FEATURE_NAME}"

# 1. 기존 worktree 확인
if git worktree list | grep -q "$WORKTREE_PATH"; then
    log_error "Worktree already exists at: $WORKTREE_PATH"
    exit 1
fi

log_info "Creating worktree for feature: ${FEATURE_NAME}"

# 2. 사용자 확인
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

# 3. 메인 리포지토리에서 feature 브랜치 생성 및 worktree 추가
log_info "Creating main worktree..."
git fetch origin
git branch "$FEATURE_BRANCH" "origin/$BASE_BRANCH" 2>/dev/null || log_warn "Branch $FEATURE_BRANCH may already exist"
git worktree add "$WORKTREE_PATH" "$FEATURE_BRANCH"

# 4. 서브모듈 초기화
log_info "Initializing submodules..."
cd "$WORKTREE_PATH"
git submodule init
git submodule update --recursive

# 5. 각 서브모듈에서 feature 브랜치 생성
log_info "Setting up submodule branches..."
for sub in "${SUBMODULES[@]}"; do
    log_info "  Processing $sub..."
    cd "$WORKTREE_PATH/$sub"

    # 원격 fetch
    git fetch origin

    # 기본 브랜치에서 feature 브랜치 생성
    DEFAULT_BRANCH=$(get_default_branch "$sub")
    if git show-ref --verify --quiet "refs/remotes/origin/$FEATURE_BRANCH"; then
        # 원격에 이미 feature 브랜치가 있으면 체크아웃
        git checkout -B "$FEATURE_BRANCH" "origin/$FEATURE_BRANCH"
        log_info "    Checked out existing remote branch"
    else
        # 없으면 기본 브랜치에서 새로 생성
        git checkout -B "$FEATURE_BRANCH" "origin/$DEFAULT_BRANCH"
        log_info "    Created new branch from $DEFAULT_BRANCH"
    fi
done

cd "$WORKTREE_PATH"

# 6. 최종 상태 출력
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
