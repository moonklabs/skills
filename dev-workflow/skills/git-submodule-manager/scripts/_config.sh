#!/bin/bash
# 공통 설정 - 서브모듈 목록, 색상, 로그 유틸리티

# 서브모듈 목록
SUBMODULES=(admin-backend backend batch)

# 서브모듈별 기본 브랜치 조회 함수
get_default_branch() {
    case "$1" in
        "admin-backend") echo "develop-ai" ;;
        "backend") echo "develop" ;;
        "batch") echo "develop" ;;
        *) echo "" ;;
    esac
}

# 색상 정의
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

# 로그 유틸리티 함수
log_info()    { echo -e "${BLUE}[INFO]${NC} $1"; }
log_success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
log_warn()    { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error()   { echo -e "${RED}[ERROR]${NC} $1"; }

# --yes 플래그 파싱 함수
# 사용: parse_yes_flag "$@"
# 결과: YES_FLAG 변수가 "true"면 비대화식 모드
parse_yes_flag() {
    YES_FLAG=false
    for arg in "$@"; do
        if [ "$arg" = "--yes" ] || [ "$arg" = "-y" ]; then
            YES_FLAG=true
        fi
    done
}

# 사용자 확인 함수 (--yes면 자동 승인)
# 사용: confirm_action "메시지" && ...
confirm_action() {
    local msg=$1
    if [ "$YES_FLAG" = "true" ]; then
        log_info "Auto-confirmed: $msg"
        return 0
    fi
    read -p "$msg (y/N): " CONFIRM
    if [[ ! "$CONFIRM" =~ ^[Yy]$ ]]; then
        log_warn "Cancelled by user"
        return 1
    fi
    return 0
}
