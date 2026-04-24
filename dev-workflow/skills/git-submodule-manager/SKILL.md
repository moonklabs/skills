---
name: git-submodule-manager
description: >
  Git worktree 생성/전환, 서브모듈 브랜치 동기화, 모노리포 커밋/푸시 관리.
  "worktree", "서브모듈", "브랜치 동기화", "feature 브랜치 생성"을 요청할 때 트리거.
---

# Worktree Manager Skill

sellerking-data-monolith 모노리포의 Git worktree 및 서브모듈을 통합 관리합니다.

## 서브모듈 매핑

| 서브모듈 | 저장소 | 기본 브랜치 |
|---------|--------|------------|
| `admin-backend` | moonklabs/sellerking-admin-backend | `develop-ai` |
| `backend` | moonklabs/sellerking-backend | `develop` |
| `batch` | moonklabs/sellerking-scraper | `develop` |

## 스크립트 경로

모든 스크립트는 플러그인 루트 기준 상대 경로:
```
skills/git-submodule-manager/scripts/
├── _config.sh    # 공통 설정 (자동 source됨)
├── create.sh     # worktree 생성
├── status.sh     # 상태 조회
├── commit.sh     # 통합 커밋
├── push.sh       # 통합 푸시
└── switch.sh     # 브랜치 전환
```

## 작업별 가이드

### CREATE - Worktree 생성

새 기능 개발을 위한 worktree 및 서브모듈 브랜치를 일괄 생성합니다.

**트리거**: "worktree 만들어줘", "새 기능 브랜치", "feature worktree 생성"

**절차**:
1. feature 이름과 베이스 브랜치 확인 (기본: main)
2. 생성될 내용 사용자에게 요약 표시:
   - Worktree 경로: `../sellerking-data-monolith-{feature-name}`
   - Main 브랜치: `feature/{feature-name}` (from main)
   - 서브모듈 브랜치: 동일 feature 브랜치
3. 사용자 확인 후 실행:
   ```bash
   bash skills/git-submodule-manager/scripts/create.sh {feature-name} {base-branch} --yes
   ```

---

### STATUS - 상태 조회

현재 worktree와 모든 서브모듈의 상태를 표시합니다.

**트리거**: "worktree 상태", "브랜치 확인", "서브모듈 상태"

**절차**:
1. 바로 실행 (확인 불필요):
   ```bash
   bash skills/git-submodule-manager/scripts/status.sh
   ```
2. 출력 분석 및 이슈 보고:
   - DETACHED HEAD → 브랜치 체크아웃 권고
   - 브랜치 불일치 → switch 명령 안내
   - 미푸시 커밋 (↑N) → push 명령 안내

---

### COMMIT - 통합 커밋

변경된 모든 서브모듈과 메인을 동일 메시지로 커밋합니다.

**트리거**: "커밋해줘", "변경사항 커밋", "commit all"

**절차**:
1. 커밋 메시지 결정:
   - 인자 있으면: 제공된 메시지 사용
   - 인자 없으면: 변경사항 분석 후 Conventional Commits 형식으로 자동 생성
     (`feat:`, `fix:`, `docs:`, `chore:` 등)
2. 변경사항 요약 표시 (서브모듈별)
3. 사용자 확인 후 실행:
   ```bash
   bash skills/git-submodule-manager/scripts/commit.sh "{commit-message}" --yes
   ```
4. **커밋 순서**: admin-backend → backend → batch → main (서브모듈 참조 포함)

---

### PUSH - 통합 푸시

미푸시 커밋이 있는 서브모듈과 메인을 원격에 푸시합니다.

**트리거**: "푸시해줘", "원격에 올려줘", "push all"

**절차**:
1. 푸시 대상 목록 표시 (미푸시 커밋 수 포함)
2. ⚠️ `--force` 요청 시: 위험성 경고 후 명시적 동의 확인
3. 사용자 확인 후 실행:
   ```bash
   bash skills/git-submodule-manager/scripts/push.sh [--force] --yes
   ```
4. **푸시 순서**: admin-backend → backend → batch → main

---

### SWITCH - 브랜치 전환

메인과 모든 서브모듈의 브랜치를 동시에 전환합니다.

**트리거**: "브랜치 전환", "브랜치 바꿔줘", "switch to", "체크아웃"

**절차**:
1. 전환할 브랜치명 및 `--create` 플래그 확인
2. 미커밋 변경사항 확인 (있으면 중단)
3. 사용자 확인 후 실행:
   ```bash
   bash skills/git-submodule-manager/scripts/switch.sh {branch-name} [--create] --yes
   ```

---

## 주의사항

- **항상 서브모듈 먼저**: commit/push 시 서브모듈 → 메인 순서 필수
- **Detached HEAD 주의**: 서브모듈 작업 전 브랜치 확인
- **`--force` 푸시**: 팀 협업 중 사용 금지, 명시적 동의 필수
- **상위 저장소 참조 업데이트**: 서브모듈 커밋 후 메인에서 참조 업데이트 자동 처리
