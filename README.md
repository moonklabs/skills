# Moonklabs Skills

뭉클랩 스킬 마켓플레이스 — 스타트업 운영, 지원사업, 개발자 워크플로, 디자인 시스템까지 **카테고리별 Claude Code 플러그인**을 한곳에서 관리합니다.  `developer-plugins`의 멀티타겟(모노리식 plugin + `skill.sh`) 패턴을 확장해, 각 카테고리가 독립 플러그인이면서 하나의 마켓플레이스로 묶입니다.

## 카테고리 구성 (6)

| 카테고리 | 플러그인 이름 | 스킬 |
|---|---|---|
| `fundraising/` | `moonklabs-fundraising` | fundraising-process · term-sheet-knowledge · deal-sourcing · investor-research · fundraise-comms · pitch-craft |
| `gtm-strategy/` | `moonklabs-gtm-strategy` | gtm-strategy · competitive-landscape · pricing-strategy · market-sizing · sales-playbook |
| `finance-metrics/` | `moonklabs-finance-metrics` | startup-metrics · financial-modeling |
| `gov-apply/` | `moonklabs-gov-apply` | kb-structure · gov-program-knowledge · bizplan-writing · hwp-format |
| `dev-workflow/` | `moonklabs-dev-workflow` | git-submodule-manager |
| `design-system/` | `moonklabs-design-system` | design-md · sprintable-design |

총 **20개 스킬**이 6개 카테고리로 묶여 있습니다.

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

## 설치

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

## skill.sh 명령

| 명령 | 설명 |
|------|------|
| `./skill.sh build` | 모든 카테고리를 순회해 `dist/AGENTS.md`와 카테고리별 요약을 포함한 `dist/codex-prompts/*.md`를 생성합니다. |
| `./skill.sh install` | `dist/codex-prompts/*.md` 를 `~/.codex/prompts/` 로 복사합니다. |
| `./skill.sh verify` | 7개 자동 테스트 (PASS/FAIL) — marketplace 검증, 카테고리별 plugin.json, SKILL.md 존재, source 경로, 빌드 성공, AGENTS.md 스모크, 이름 충돌 없음. |
| `./skill.sh check` | plugin.json/SKILL.md 형식을 린트합니다. |

## 스킬 추가/수정

1. 적절한 카테고리 선택 (`fundraising/`, `gtm-strategy/`, ...).
2. `<category>/skills/<new-skill>/SKILL.md` 를 추가하거나 기존 SKILL.md를 편집.
3. 해당 카테고리 `<category>/.claude-plugin/plugin.json` 의 `skills` 배열에 등록.
4. 새 카테고리가 필요하면 `.claude-plugin/marketplace.json` 에 플러그인 항목을 추가.
5. `./skill.sh verify` 통과 확인 → `./skill.sh build && ./skill.sh install` 로 Codex 반영.

## 수동 검증

### Claude Code
1. 마켓플레이스 등록 후 `/plugin list`에서 6개 플러그인이 노출되는지 확인.
2. 최소 한 카테고리를 설치 → 대표 스킬이 트리거되는지 테스트 (예: "피치 덱 만들기", "DESIGN.md 만들어줘").

### Codex CLI
1. `./skill.sh build && ./skill.sh install` 실행 후 `ls ~/.codex/prompts/` 에 20개 파일 확인.
2. Codex CLI에서 스킬 이름을 참조해 1회 호출이 성공하는지 확인.

## 출처

- `fundraising/`, `gtm-strategy/`, `finance-metrics/` 카테고리: `startup-plugins/startup-fundraise/skills/` 에서 재분류.
- `gov-apply/` 카테고리: `startup-plugins/startup-apply/skills/` 에서 이관.
- `dev-workflow/`, `design-system/` 카테고리: `developer-plugins/skills/` 에서 이관.

## 로드맵

- GitHub Actions CI로 `skill.sh verify` 자동 실행
- GitHub Release 에 `dist/` 산출물 업로드
- `skill.sh uninstall` 구현 (설치된 Codex 프롬프트 제거)
- 카테고리 단위 버전 관리 + changelog 자동화
- 외부 공개 마켓플레이스 등재

## 라이선스

[LICENSE](./LICENSE) 참조.
