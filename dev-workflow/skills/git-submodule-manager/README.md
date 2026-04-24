# git-submodule-manager

sellerking-data-monolith의 Git worktree + submodule 통합 관리 Claude Code 플러그인.

## 개요

이 플러그인은 3개의 git submodule(admin-backend, backend, batch)을 포함한 모노리포에서 worktree 생명주기를 통합 관리합니다.

## 설치

```bash
# 1. 로컬 마켓플레이스 등록
/plugin marketplace add /Users/drumcap/workspace/sellerking-data-monolith/git-submodule-manager

# 2. 플러그인 설치
/plugin install git-submodule-manager@git-submodule-manager-dev

# 3. Claude Code 재시작 후 사용
```

## 커맨드 목록

| 커맨드 | 설명 | 인자 |
|--------|------|------|
| `/git-submodule-manager:create` | 새 feature worktree 생성 | `<feature-name> [base-branch]` |
| `/git-submodule-manager:status` | 전체 worktree/서브모듈 상태 조회 | - |
| `/git-submodule-manager:commit` | 모든 서브모듈+메인 통합 커밋 | `[커밋 메시지]` |
| `/git-submodule-manager:push` | 모든 서브모듈+메인 통합 푸시 | `[--force]` |
| `/git-submodule-manager:switch` | 모든 서브모듈+메인 브랜치 전환 | `<브랜치명> [--create]` |

## Skill 자동 트리거

다음 키워드로 대화할 때 `worktree-manager` skill이 자동으로 활성화됩니다:
- "worktree 만들어줘", "새 feature 브랜치"
- "worktree 상태 확인", "브랜치 확인"
- "커밋해줘", "변경사항 커밋"
- "푸시해줘", "원격에 올려줘"
- "브랜치 전환", "브랜치 바꿔줘"

## 아키텍처

```
git-submodule-manager/
├── .claude-plugin/
│   ├── plugin.json          # 플러그인 메타데이터
│   └── marketplace.json     # 로컬 개발 마켓플레이스
├── skills/
│   └── worktree-manager/
│       ├── SKILL.md         # 디스패처 skill 정의
│       ├── scripts/
│       │   ├── _config.sh   # 공통 설정 (서브모듈 목록, 색상, 유틸)
│       │   ├── create.sh    # worktree 생성
│       │   ├── status.sh    # 상태 조회
│       │   ├── commit.sh    # 통합 커밋
│       │   ├── push.sh      # 통합 푸시
│       │   └── switch.sh    # 브랜치 전환
│       └── references/
│           └── submodule-map.md  # 서브모듈 브랜치 매핑 참조
├── commands/                # Slash commands (thin wrappers)
│   ├── create.md
│   ├── status.md
│   ├── commit.md
│   ├── push.md
│   └── switch.md
└── README.md
```

## 서브모듈 매핑

| 경로 | 기본 브랜치 |
|------|------------|
| `admin-backend` | `develop-ai` |
| `backend` | `develop` |
| `batch` | `develop` |

## 직접 스크립트 실행

```bash
# 상태 조회
bash skills/git-submodule-manager/scripts/status.sh

# worktree 생성 (비대화식)
bash skills/git-submodule-manager/scripts/create.sh my-feature main --yes

# 통합 커밋 (비대화식)
bash skills/git-submodule-manager/scripts/commit.sh "feat: add feature" --yes

# 통합 푸시 (비대화식)
bash skills/git-submodule-manager/scripts/push.sh --yes

# 브랜치 전환
bash skills/git-submodule-manager/scripts/switch.sh feature/my-feature --yes
```

`--yes` 플래그: 모든 확인 프롬프트를 자동 승인 (Claude에서 비대화식 실행 시 필수)
