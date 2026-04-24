#!/bin/bash
# Shared config — submodule list, colors, logging utilities

# Submodule list
SUBMODULES=(admin-backend backend batch)

# Returns the default branch for a given submodule
get_default_branch() {
    case "$1" in
        "admin-backend") echo "develop-ai" ;;
        "backend") echo "develop" ;;
        "batch") echo "develop" ;;
        *) echo "" ;;
    esac
}

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

# Logging utilities
log_info()    { echo -e "${BLUE}[INFO]${NC} $1"; }
log_success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
log_warn()    { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error()   { echo -e "${RED}[ERROR]${NC} $1"; }

# Parses --yes / -y flag from args
# Usage: parse_yes_flag "$@"
# Result: sets YES_FLAG to "true" when non-interactive mode is requested
parse_yes_flag() {
    YES_FLAG=false
    for arg in "$@"; do
        if [ "$arg" = "--yes" ] || [ "$arg" = "-y" ]; then
            YES_FLAG=true
        fi
    done
}

# Interactive confirmation helper (auto-approves when --yes is set)
# Usage: confirm_action "message" && ...
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
