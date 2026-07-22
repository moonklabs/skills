#!/bin/bash
# Shared config — submodule discovery, colors, logging utilities
#
# Submodule list and per-submodule default branches are auto-detected from
# .gitmodules, so this file works unmodified in any repo with git submodules.
# To pin a submodule's default branch explicitly, use git's own mechanism:
#   git submodule set-branch --branch <branch> <path>
# (writes a `branch = ...` entry into .gitmodules — no custom config needed)

# Auto-detect submodule paths + any declared default branch from .gitmodules.
# Overrides are kept as "path<TAB>branch" lines in a plain string rather than
# an associative array: macOS ships bash 3.2 as /bin/bash, and `declare -A`
# there exits non-zero — which, under `set -e` in the scripts that source
# this file, aborts the whole script before it does anything.
SUBMODULES=()
_SUBMODULE_BRANCH_OVERRIDES=""
if [ -f .gitmodules ]; then
    while read -r name path; do
        [ -z "$path" ] && continue
        SUBMODULES+=("$path")
        branch=$(git config --file .gitmodules --get "submodule.$name.branch" 2>/dev/null)
        if [ -n "$branch" ]; then
            _SUBMODULE_BRANCH_OVERRIDES="$_SUBMODULE_BRANCH_OVERRIDES$path	$branch
"
        fi
    done < <(git config --file .gitmodules --get-regexp '^submodule\..*\.path$' 2>/dev/null | sed -E 's/^submodule\.(.+)\.path (.+)$/\1 \2/')
fi

# Returns the default branch for a given submodule path:
#   1. .gitmodules `branch =` override (set via `git submodule set-branch`)
#   2. the submodule's remote HEAD, read locally first (no network round trip),
#      falling back to a live `git remote show origin` query
get_default_branch() {
    local path=$1
    local override
    override=$(printf '%s' "$_SUBMODULE_BRANCH_OVERRIDES" | awk -F'\t' -v p="$path" '$1 == p {print $2; exit}')
    if [ -n "$override" ]; then
        echo "$override"
        return
    fi
    [ -d "$path" ] || return
    local head_ref
    head_ref=$(git -C "$path" symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null)
    if [ -n "$head_ref" ]; then
        echo "${head_ref#origin/}"
        return
    fi
    git -C "$path" remote show origin 2>/dev/null | awk '/HEAD branch/ {print $NF}'
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

# Parses --quiet / -q flag from args
# Usage: parse_quiet_flag "$@"
# Result: sets QUIET_FLAG to "true" when compact output is requested.
# Claude should default to --quiet for routine checks (status, commit preview)
# and only fall back to full output when the user asks to see details —
# it cuts the tokens spent re-reading tool output by a large margin.
parse_quiet_flag() {
    QUIET_FLAG=false
    for arg in "$@"; do
        if [ "$arg" = "--quiet" ] || [ "$arg" = "-q" ]; then
            QUIET_FLAG=true
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
