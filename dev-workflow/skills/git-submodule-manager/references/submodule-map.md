# Submodule Branch Mapping

## 서브모듈 정보

| 경로 | 저장소 | 기본 브랜치 | 설명 |
|------|--------|------------|------|
| `admin-backend` | moonklabs/sellerking-admin-backend | `develop-ai` | NestJS 관리자 API |
| `backend` | moonklabs/sellerking-backend | `develop` | NestJS 메인 API |
| `batch` | moonklabs/sellerking-scraper | `develop` | 스크래핑 배치 |

## 브랜치 전략

### Feature 브랜치
- 형식: `feature/{feature-name}`
- 예시: `feature/batch-queue-prd`, `feature/user-auth`
- 생성 위치: main + 모든 서브모듈에 동일하게 생성

### 서브모듈별 기본 브랜치 (feature 브랜치 없을 때 베이스)
- `admin-backend`: `develop-ai` — AI 기능 개발용
- `backend`: `develop` — 메인 API 개발
- `batch`: `develop` — 배치/스크래퍼 개발

### 브랜치 생성 규칙
1. 원격에 해당 feature 브랜치가 이미 있으면 → 원격 브랜치에서 체크아웃
2. 원격에 없으면 → 서브모듈별 기본 브랜치에서 새로 생성

## Worktree 경로 규칙

```
../sellerking-data-monolith-{feature-name}/
├── admin-backend/      # 서브모듈 (feature 브랜치)
├── backend/            # 서브모듈 (feature 브랜치)
├── batch/              # 서브모듈 (feature 브랜치)
└── ...                 # 메인 리포 파일들
```

## Commit/Push 순서

서브모듈 참조 무결성을 위해 반드시 이 순서로 진행:

1. `admin-backend` (변경사항 있을 때)
2. `backend` (변경사항 있을 때)
3. `batch` (변경사항 있을 때)
4. `main` — 서브모듈 참조(`.gitmodules` 포인터) + 기타 변경사항

## 주의사항

- 서브모듈은 특정 커밋 SHA를 가리킴 → 서브모듈 커밋 후 반드시 메인에서 참조 업데이트
- 서브모듈 작업 전 `git checkout {branch}` 로 브랜치 확인 (Detached HEAD 방지)
- 모노리포 루트에서 `git submodule update --init --recursive` 로 초기화 확인
