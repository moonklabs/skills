# Moonklabs Skills

뭉클랩 스킬 마켓플레이스 — 스타트업 운영, 지원사업, 개발자 워크플로, 디자인 시스템까지 **카테고리별 Claude Code 플러그인**을 한곳에서 관리합니다. `developer-plugins`의 멀티타겟(모노리식 plugin + `skill.sh`) 패턴을 확장해, 각 카테고리가 독립 플러그인이면서 하나의 마켓플레이스로 묶입니다.

## 설치 방법 2가지

| 방법 | 대상 | 특징 |
|---|---|---|
| **`npx skills`** | Claude Code, Codex, Cursor 등 [skills.sh](https://skills.sh) 지원 에이전트 전체 | 저장소를 클론할 필요 없이 카테고리·스킬 단위로 한 줄 설치 |
| **플러그인 추가** | **Claude Code**, **Codex** | 저장소를 마켓플레이스/프롬프트 소스로 직접 등록하는 네이티브 방식. Claude Code는 `/plugin` → Add Marketplace, Codex는 `skill.sh`로 `~/.codex/prompts/`에 설치 |

아래 "카테고리별 설치"는 `npx skills`, "플러그인 방식 설치"는 Claude Code·Codex 네이티브 방법을 다룹니다.

## 카테고리 구성 (6)

| 카테고리 | 플러그인 이름 | 스킬 수 |
|---|---|---|
| `fundraising/` | `moonklabs-fundraising` | 6 |
| `gtm-strategy/` | `moonklabs-gtm-strategy` | 5 |
| `finance-metrics/` | `moonklabs-finance-metrics` | 2 |
| `gov-apply/` | `moonklabs-gov-apply` | 4 |
| `dev-workflow/` | `moonklabs-dev-workflow` | 4 |
| `design-system/` | `moonklabs-design-system` | 2 |

총 **23개 스킬**이 6개 카테고리로 묶여 있습니다.

## 카테고리별 설치 (`npx skills`)

카테고리 전체를 한 번에 설치하거나, `--skill` 뒤 이름을 골라 개별 스킬만 설치할 수 있습니다. `--global`을 빼면 현재 프로젝트에만 설치됩니다.

### `fundraising/` — moonklabs-fundraising

```bash
npx skills add moonklabs/skills --skill fundraising-process term-sheet-knowledge deal-sourcing investor-research fundraise-comms pitch-craft --global
```

| 스킬 | 무엇을 하나요 |
|---|---|
| `fundraising-process` | 프리시드~시리즈B 투자유치 라이프사이클 — 단계별 벤치마크, 8주 타임라인, 준비 체크리스트 |
| `term-sheet-knowledge` | 텀시트 핵심 조항, SAFE/전환사채 구조, 캡테이블 희석 계산, 레드플래그 |
| `deal-sourcing` | VC·AC·엔젤·CVC 투자자 소싱 방법론과 데이터 소스 |
| `investor-research` | VC 펀드/파트너 리서치 — thesis 매칭, 포트폴리오 분석, 접근 전략 |
| `fundraise-comms` | 투자자 이메일 템플릿(웜인트로/콜드/팔로업), 월간 업데이트, Day5/10/21 케이던스 |
| `pitch-craft` | 세쿼이아 스타일 피치덱 구조, 슬라이드 가이드, 스토리텔링, 예상 VC 질문 30개 |

### `gtm-strategy/` — moonklabs-gtm-strategy

```bash
npx skills add moonklabs/skills --skill gtm-strategy competitive-landscape pricing-strategy market-sizing sales-playbook --global
```

| 스킬 | 무엇을 하나요 |
|---|---|
| `gtm-strategy` | Go-to-Market 전략 — GTM 모션, 콘텐츠 전략, 채널 선택, 브랜드 빌딩 |
| `competitive-landscape` | 경쟁 환경 분석, 포지셔닝 전략, 배틀카드 작성 |
| `pricing-strategy` | 가격 전략과 패키징 — 가격 모델, 가치 지표, 가격 심리학 |
| `market-sizing` | TAM/SAM/SOM 시장 규모 분석 (Top-down · Bottom-up · Value Theory) |
| `sales-playbook` | B2B 세일즈 프로세스 — MEDDPICC, 세일즈 단계, 팀 설계 |

### `finance-metrics/` — moonklabs-finance-metrics

```bash
npx skills add moonklabs/skills --skill startup-metrics financial-modeling --global
```

| 스킬 | 무엇을 하나요 |
|---|---|
| `startup-metrics` | 비즈니스 모델(SaaS/마켓플레이스/컨슈머/B2B)별 핵심 지표 프레임워크와 단계별 벤치마크 |
| `financial-modeling` | Base/Bull/Bear 3-시나리오 재무 모델링, 유닛 이코노믹스(CAC/LTV), 코호트 분석, 런웨이 계산 |

### `gov-apply/` — moonklabs-gov-apply

```bash
npx skills add moonklabs/skills --skill kb-structure gov-program-knowledge bizplan-writing hwp-format --global
```

| 스킬 | 무엇을 하나요 |
|---|---|
| `kb-structure` | 회사 지식베이스 구조화, 스키마 정의, 완성도 검증 |
| `gov-program-knowledge` | 한국 정부·민간 지원사업 공고 시스템, 평가 기준, 프로그램 특성(TIPS·예비창업패키지 등) 지식 |
| `bizplan-writing` | 한국 정부지원사업 사업계획서(事業計劃書) 작성 도메인 지식 |
| `hwp-format` | HWP/HWPX 파일 형식과 한글 정부 문서 서식 가이드 |

### `dev-workflow/` — moonklabs-dev-workflow

```bash
npx skills add moonklabs/skills --skill git-submodule-manager explain-diff-html explain-diff-html-plain explain-plan-html --global
```

| 스킬 | 무엇을 하나요 |
|---|---|
| `git-submodule-manager` | Git worktree 생성/전환, 서브모듈 브랜치 동기화, 모노리포 커밋/푸시 관리 |
| `explain-diff-html` | 코드 변경·PR·브랜치 diff를 마크다운 + 다이어그램 DSL로 작성하면 CSS/JS/목차/퀴즈까지 렌더러가 자동 처리해 대화형 HTML 해설서를 만듭니다 |
| `explain-diff-html-plain` | 위 스킬의 렌더러 없이 HTML을 직접 작성하는 순수판 — DSL로 표현 못 하는 자유 레이아웃이 필요하거나 Python을 쓸 수 없을 때 |
| `explain-plan-html` | 작업 계획(plan) 파일을 승인 판단용 브리핑(brief) 또는 실행 추적용 풀 버전(full) HTML 해설서로 변환 |

하나만 설치하려면:

```bash
npx skills add moonklabs/skills --skill explain-diff-html --global
```

### `design-system/` — moonklabs-design-system

```bash
npx skills add moonklabs/skills --skill design-md sprintable-design --global
```

| 스킬 | 무엇을 하나요 |
|---|---|
| `design-md` | Stitch(Google Labs) `design.md` 알파 스펙을 준수하는 DESIGN.md 파일을 프로젝트 토큰·컴포넌트 자동 탐색으로 생성 |
| `sprintable-design` | Sprintable 브랜드 UI 키트 — 컬러·타이포·폰트·에셋으로 프로덕션/프로토타입 인터페이스 생성 |

설치 후 각 에이전트에서 표에 적힌 트리거 문구(예: "피치 덱 만들기", "DESIGN.md 만들어줘", "이 PR 해설 만들어줘")를 말하면 자동으로 해당 스킬이 실행됩니다.

## 플러그인 방식 설치 (Claude Code / Codex)

`npx skills` 없이 저장소를 직접 플러그인/프롬프트 소스로 등록하는 방법입니다. **Claude Code와 Codex는 이 네이티브 플러그인 추가 방식을 지원합니다.**

### Claude Code (canonical)

1. 이 저장소를 클론하거나 경로를 준비합니다.
2. `/plugin` 메뉴 → **Add Marketplace** → 이 저장소의 절대 경로(예: `/Users/you/workspace_plugin/skills`)를 입력.
3. `/plugin` 에서 원하는 카테고리 플러그인을 개별 설치 (`moonklabs-fundraising`, `moonklabs-gtm-strategy` 등) 또는 필요한 것만 골라 설치합니다.
4. 설치된 플러그인에 속한 스킬은 이름 자동 트리거 또는 `/skill:<name>` 형태로 호출됩니다.

### Codex CLI (via skill.sh)

사전 요구사항: `yq`, `jq` — macOS에서는 `brew install yq jq`.

```bash
./skill.sh build      # dist/AGENTS.md + dist/codex-prompts/*.md 생성
./skill.sh install    # ~/.codex/prompts/ 로 복사
```

설치 후 Codex CLI에서 스킬 이름(`fundraising-process`, `pitch-craft`, `git-submodule-manager` 등)으로 프롬프트를 참조할 수 있습니다. 각 스킬의 SKILL.md를 수정한 뒤 `./skill.sh build`로 재빌드하세요.

## 저장소 구조

```
skills/
├── .claude-plugin/
│   └── marketplace.json            # 6개 플러그인을 등록하는 마켓플레이스
├── fundraising/
│   ├── .claude-plugin/plugin.json
│   └── skills/
│       ├── fundraising-process/SKILL.md
│       ├── term-sheet-knowledge/SKILL.md
│       └── ...
├── gtm-strategy/            (동일 구조)
├── finance-metrics/         (동일 구조)
├── gov-apply/               (동일 구조)
├── dev-workflow/            (동일 구조)
├── design-system/           (동일 구조; assets/preview/ui_kits 포함)
├── skill.sh                 # build / install / verify / check
├── dist/                    # 빌드 산출물 (gitignored)
├── LICENSE
└── README.md
```

## skill.sh 명령

| 명령 | 설명 |
|------|------|
| `./skill.sh build` | 모든 카테고리를 순회해 `dist/AGENTS.md`와 카테고리별 요약을 포함한 `dist/codex-prompts/*.md`를 생성합니다. |
| `./skill.sh install` | `dist/codex-prompts/*.md` 를 `~/.codex/prompts/` 로 복사합니다. |
| `./skill.sh verify` | 7개 자동 테스트 (PASS/FAIL) — marketplace 검증, 카테고리별 plugin.json, `skills/` 디렉터리와 SKILL.md 존재, 빌드 성공, AGENTS.md 스모크, 이름 충돌 없음. |
| `./skill.sh check` | plugin.json/SKILL.md 형식을 린트합니다. |

## 스킬 추가/수정

1. 적절한 카테고리 선택 (`fundraising/`, `gtm-strategy/`, ...).
2. `<category>/skills/<new-skill>/SKILL.md` 를 추가하거나 기존 SKILL.md를 편집.
3. Claude Code는 카테고리 루트의 `skills/`를 자동 탐색하므로 별도 manifest 등록은 필요 없습니다.
4. 새 카테고리가 필요하면 `.claude-plugin/marketplace.json` 에 플러그인 항목을 추가.
5. `./skill.sh verify` 통과 확인 → `./skill.sh build && ./skill.sh install` 로 Codex 반영.

## 수동 검증

### npx skills
1. 카테고리 명령 실행 후 대상 에이전트(Claude Code/Codex/Cursor)에서 스킬 이름 또는 트리거 문구로 1회 호출.

### Claude Code
1. 마켓플레이스 등록 후 `/plugin list`에서 6개 플러그인이 노출되는지 확인.
2. 최소 한 카테고리를 설치 → 대표 스킬이 트리거되는지 테스트 (예: "피치 덱 만들기", "DESIGN.md 만들어줘").

### Codex CLI
1. `./skill.sh build && ./skill.sh install` 실행 후 `ls ~/.codex/prompts/` 에 23개 파일 확인.
2. Codex CLI에서 스킬 이름을 참조해 1회 호출이 성공하는지 확인.

## 출처

- `fundraising/`, `gtm-strategy/`, `finance-metrics/` 카테고리: `startup-plugins/startup-fundraise/skills/` 에서 재분류.
- `gov-apply/` 카테고리: `startup-plugins/startup-apply/skills/` 에서 이관.
- `dev-workflow/`, `design-system/` 카테고리: `developer-plugins/skills/` 에서 이관.
- `dev-workflow/explain-diff-html`, `explain-diff-html-plain`, `explain-plan-html`: 개인 스킬 폴더(`~/.claude/skills/`)에서 복사.

## 로드맵

- GitHub Actions CI로 `skill.sh verify` 자동 실행
- GitHub Release 에 `dist/` 산출물 업로드
- `skill.sh uninstall` 구현 (설치된 Codex 프롬프트 제거)
- 카테고리 단위 버전 관리 + changelog 자동화
- 외부 공개 마켓플레이스 등재

## 라이선스

[LICENSE](./LICENSE) 참조.
