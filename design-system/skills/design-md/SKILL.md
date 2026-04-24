---
name: design-md
version: 1.0.0
description: |
  Stitch(Google Labs) design.md alpha 스펙을 준수하는 DESIGN.md 파일을 생성한다.
  프로젝트의 디자인 토큰 · 컴포넌트 · 브랜드 맥락을 자동 탐색한 뒤
  YAML frontmatter(기계 판독용) + 표준 8섹션 markdown(인간 판독용) 으로 작성한다.
  Claude Code · Cursor · Stitch · AI 코딩 에이전트 모두 동일하게 이해하는 단일 디자인 진리의 원천.
  사용 시점: "DESIGN.md 만들어줘", "디자인 시스템 문서화", "design.md 스펙", "Stitch 포맷 디자인 문서"
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash
  - AskUserQuestion
  - WebFetch
triggers:
  - DESIGN.md 생성
  - 디자인 md 파일
  - design.md
  - Stitch 디자인 스펙
  - 디자인 시스템 문서
  - 디자인 토큰 문서화
---

# design-md · Stitch 스펙 DESIGN.md 생성기

## 0. 핵심 원칙

이 스킬은 **Google Labs [`@google/design.md`](https://github.com/google-labs-code/design.md) alpha 스펙** 을 그대로 따른다.

생성되는 `DESIGN.md` 는 다음 두 계층으로 구성된다:

| 계층 | 형식 | 역할 |
|---|---|---|
| **YAML Frontmatter** | `---` 로 감싼 YAML | 기계 판독 (Stitch · 린터 · 자동 export) |
| **Markdown Body** | `##` h2 섹션 8개 | 인간 판독 (설계 의도 · 사용 가이드) |

**반드시 지킬 것:**
- 섹션 순서 고정: Overview → Colors → Typography → Layout → Elevation & Depth → Shapes → Components → Do's and Don'ts
- 토큰 참조 문법은 `{colors.primary}`, `{typography.h1}`, `{spacing.4}` 형태 (중괄호 + dot notation)
- 색상은 `#` + hex(sRGB), dimension 은 `px|rem|em` 단위 포함
- Primary 컬러 **반드시** 정의
- 불필요한 섹션은 생략 가능하지만 존재하면 순서를 지켜야 함

---

## 1. 워크플로우

사용자가 이 스킬을 호출하면 아래 5단계를 **순차적으로** 수행한다.

### Phase 1 · 프로젝트 탐색 (Discovery)

병렬로 다음 패턴을 스캔한다:

```bash
# 디자인 토큰 소스 후보
src/design-system/**/*.{ts,js,json}
src/theme/**/*.{ts,js}
src/**/tokens*.{ts,js,json}
tailwind.config.{js,ts,cjs,mjs}
src/**/design-tokens.*
tokens.json
tokens-studio.json
src/**/variables.css
src/**/theme.{ts,js}

# 컴포넌트 위치 후보
src/design-system/ui/**/*.{tsx,ts}
src/components/ui/**/*.{tsx,ts}
src/components/**/*.{tsx,ts}
packages/ui/**/*.{tsx,ts}

# 기존 디자인 문서
DESIGN.md
docs/design.md
docs/DESIGN-SYSTEM.md
STYLEGUIDE.md
```

**탐색 결과를 분류한다:**

1. **Single-source token file 발견** → 직접 파싱 (예: `source.js`, `tokens.ts`, `theme.ts`)
2. **Tailwind config 발견** → theme.extend 파싱
3. **CSS variables 발견** → `:root { --color-* }` grep
4. **MUI theme 발견** → `createTheme({ palette, typography })` 파싱
5. **전부 없음** → 인터뷰 모드 진입 (Phase 2b)

### Phase 2a · 토큰 자동 추출

찾은 소스에서 다음을 추출:

| 항목 | 최소 필수 | 추가로 수집 |
|---|---|---|
| **colors** | primary | secondary · accent · success · warning · error · info · text/bg/border |
| **typography** | h1, body | h2~h6, caption, display, numeric |
| **spacing** | 기본 scale (4/8/16px 등) | 전체 scale |
| **rounded** | sm/md/lg | full, xl+ |
| **components** | button, input, card | 프로젝트 고유 컴포넌트 |

### Phase 2b · 인터뷰 (토큰이 불충분할 때)

`AskUserQuestion` 으로 아래 질문을 **그룹핑**하여 최대 4개까지 묻는다:

1. **Brand Personality**: 어떤 톤? (professional/playful/minimal/editorial/brutalist/…)
2. **Primary Color**: 주요 브랜드 컬러 hex 값?
3. **Target Users**: 누가, 어떤 맥락에서 사용하는 제품인가?
4. **Typography Preference**: 폰트 체계에 대한 구체적 요구? (특정 폰트, 한/영/숫자 분리, Weight 제약)

### Phase 3 · YAML Frontmatter 생성

아래 **정확한 순서와 필드**로 작성한다:

```yaml
---
version: alpha
name: <제품명>
description: >
  <2~4줄. 제품 정체성, 타깃 사용자, 디자인 언어의 핵심>

colors:
  # Brand
  primary: "#xxxxxx"
  primary-dark: "#xxxxxx"
  primary-light: "#xxxxxx"
  secondary: "#xxxxxx"
  accent: "#xxxxxx"

  # Status (4종 필수)
  success: "#xxxxxx"
  warning: "#xxxxxx"
  error: "#xxxxxx"
  info: "#xxxxxx"

  # Text (primary/secondary/muted/disabled/inverse 최소 5종)
  text-primary: "#xxxxxx"
  text-secondary: "#xxxxxx"
  text-muted: "#xxxxxx"
  text-disabled: "#xxxxxx"
  text-inverse: "#xxxxxx"

  # Background (primary/secondary/hover/selected 최소 4종)
  bg-primary: "#xxxxxx"
  bg-secondary: "#xxxxxx"
  bg-hover: "#xxxxxx"

  # Border
  border: "#xxxxxx"
  border-focus: "#xxxxxx"

typography:
  # 최소 base + h1~h3, 가능하면 9~15 levels
  caption:
    fontFamily: <Font>
    fontSize: 1.2rem
    fontWeight: 400
    lineHeight: 1.4
  body:
    fontFamily: <Font>
    fontSize: 1.4rem
    fontWeight: 400
    lineHeight: 1.5
  h1:
    fontFamily: <DisplayFont>
    fontSize: 3.2rem
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.02em
  # … h2, h3, numeric variants

rounded:
  none: 0
  sm: 2px
  DEFAULT: 4px
  md: 6px
  lg: 8px
  full: 9999px

spacing:
  "0": 0
  "1": 4px
  "2": 8px
  "3": 12px
  "4": 16px
  "6": 24px
  "8": 32px

components:
  # 발견된 컴포넌트마다 하나씩
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.text-inverse}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    height: 40px
    padding: 0 16px
  button-secondary:
    backgroundColor: "{colors.bg-primary}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    rounded: "{rounded.md}"
  input:
    backgroundColor: "{colors.bg-primary}"
    borderColor: "{colors.border}"
    rounded: "{rounded.DEFAULT}"
    height: 40px
  card:
    backgroundColor: "{colors.bg-primary}"
    rounded: "{rounded.lg}"
    padding: 20px
---
```

**토큰 참조 규칙:**
- 값 대신 다른 토큰을 참조할 때는 반드시 `"{category.name}"` 형식
- 문자열로 감싸기 (YAML 파서 호환성)
- 중첩 참조는 1단계까지만 (토큰 → 토큰 → 토큰 금지)

### Phase 4 · Markdown Body 8섹션 작성

각 섹션의 **필수 구성요소:**

#### ① Overview

- Brand Personality 표 (Tone / Density / Color / Voice / Target · 4~5축)
- Emotional Response 3~5개 (사용자가 느껴야 할 감정)
- Core Design Principles 5개 이내
- **Anti-Patterns** (What this is NOT) — 의도적으로 피하는 것들

#### ② Colors

- Palette Hierarchy 도식 (어떤 카테고리가 몇 개 토큰으로 구성되는지)
- Primary 의 single-source-of-truth 역할 강조
- Status 4종 사용 원칙 (언제 어떤 색을 쓰는가)
- **WCAG 접근성 대비 비율 표** (최소 3~5 조합)
- Text / Background / Border 각 토큰 표

#### ③ Typography

- Font Stack 선택 근거 (왜 이 폰트인가, 언제 쓰는가)
- fallback chain
- Scale 전체 표 (Token / Size / Line-Height / Weight / 용도)
- Numeric Variant 별도 섹션 (tabular-nums 필요 시)
- Usage Heuristic — ✅/❌ 룰 5~8개

#### ④ Layout

- Breakpoints 표
- Container 전략 (max-width, gutter)
- Spacing Scale 전체
- Spacing Application Heuristic 표 (상황별 권장 간격)
- Grid System (Flexbox vs CSS Grid 분기 기준)
- Component Dimensions 표 (height sizes matrix)
- Z-Index Semantic 계층

#### ⑤ Elevation & Depth

- Philosophy 선언 (flat vs material, subtle vs dramatic)
- Shadow Tokens 전체 표
- **Status Glow Shadow** (있을 경우)
- Elevation Hierarchy 도식 (Z-elev 0~5)
- Motion Tokens (duration · easing)
- Opacity Scale

#### ⑥ Shapes

- Corner Radius Scale 전체 표
- Shape Language 선언 (4px 기본? 8px? 0?)
- Border Width 규칙
- **Shape-to-Component Mapping 표** (어떤 컴포넌트가 어떤 radius 를 쓰는지)

#### ⑦ Components

각 주요 컴포넌트에 대해:

- 파일 경로
- 기본 API (props 표)
- 사용 예시 코드 (실제 코드, 가상 금지)
- 토큰 참조 (`{components.xxx}`)
- Variants / Presets 표
- 디자인 의도 설명

순서: Button → Input/Field → Select/Combobox → Checkbox → Radio → Modal → Card → Tag → Table → Navigation → Custom

#### ⑧ Do's and Don'ts

- ✅ Do: 7~12개 (각 항목은 *원칙 + 코드 예시*)
- ❌ Don't: 7~12개 (각 항목은 *안티 패턴 + 올바른 대안*)

카테고리 커버리지:
- 토큰 참조
- 단위 (px vs rem)
- Primary 사용 제약
- 접근성 (focus ring, 대비)
- Z-Index 의미론
- Deprecated 사용 금지

### Phase 5 · Appendix & 검증

**Appendix 에 포함:**
1. Token 치트시트 (CSS Variables / Tailwind class / 프레임워크 theme)
2. Import 치트시트 (주요 컴포넌트 import 경로)
3. 기여 가이드 (새 토큰 / 새 컴포넌트 추가 워크플로우)
4. 린팅 명령어:
   ```bash
   npx @google/design.md lint DESIGN.md
   npx @google/design.md export --format tailwind DESIGN.md
   npx @google/design.md diff DESIGN.md DESIGN-v2.md
   ```

**자체 검증 체크리스트 (출력 전 반드시 통과):**

- [ ] YAML frontmatter 가 `---` 로 열고 닫힘
- [ ] `name` · `colors.primary` · `typography` 정의됨
- [ ] 8 섹션이 정확한 순서
- [ ] 섹션 중복 없음
- [ ] 토큰 참조(`{...}`)가 실제 존재하는 토큰을 가리킴
- [ ] hex 값은 `#` + 6자리
- [ ] dimension 은 단위(px/rem/em) 포함 또는 0
- [ ] h1 타이틀은 선택, `##` 이 주된 섹션 레벨
- [ ] Primary 와 본문 대비 WCAG AA 이상

---

## 2. 출력 경로

기본값: `<project-root>/DESIGN.md` 또는 `<project-root>/src/design-system/DESIGN.md`

**결정 룰:**
1. `src/design-system/` 폴더가 이미 있으면 → 그 안에 생성
2. 없으면 프로젝트 루트에 생성
3. 사용자가 명시적으로 경로를 지정했으면 → 그 경로 사용

---

## 3. 언어 정책

- 프로젝트의 `CLAUDE.md` 또는 README 에서 주 언어 감지
- 한국어 프로젝트(CLAUDE.md 에 "always use korean" 등이 있으면) → **한국어로 작성**
- 영어 프로젝트 → **영어로 작성**
- YAML frontmatter 의 key 는 **항상 영어 snake-case**

---

## 4. 호출 예시

### 4.1 기본 호출
```
/design-md
```
현재 디렉토리 스캔 → `DESIGN.md` 생성

### 4.2 경로 지정
```
/design-md --output src/design-system/DESIGN.md
```

### 4.3 기존 파일 업데이트
```
/design-md --update
```
기존 `DESIGN.md` 의 섹션을 유지하면서 토큰/컴포넌트만 재추출해서 병합

### 4.4 최소 스켈레톤만 생성
```
/design-md --skeleton
```
인터뷰 없이 플레이스홀더로 채운 빈 템플릿만 생성

---

## 5. 안티 패턴 (이 스킬이 하지 말아야 할 것)

- ❌ 존재하지 않는 컴포넌트를 컴포넌트 섹션에 상상으로 추가
- ❌ 실제 프로젝트 토큰이 아닌 "추천 팔레트" 만들기
- ❌ 섹션 순서 임의 변경
- ❌ `{colors.xxx}` 토큰 참조를 쓰면서 실제로 그 토큰이 정의되지 않음
- ❌ 한국어 프로젝트인데 본문을 영어로 작성
- ❌ 기존 `DESIGN.md` 를 백업 없이 덮어쓰기 (update 모드 아닌 경우 덮어쓰기 전 확인)

---

## 6. 참고 자료

- Spec Repo: https://github.com/google-labs-code/design.md
- Spec Doc: https://github.com/google-labs-code/design.md/blob/main/docs/spec.md
- Stitch Official: https://stitch.withgoogle.com/docs/design-md/
- Blog: https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-design-md/

---

## 7. 완료 보고 포맷

작업 완료 시 아래 형식으로 사용자에게 보고:

```markdown
## ✅ DESIGN.md 생성 완료

**경로:** <path>
**크기:** <NNkb, NN lines>
**스펙:** Stitch design.md alpha

### 📊 추출 결과
- Colors: <n> 토큰 (primary/status/text/bg/border/chart)
- Typography: <n> 레벨
- Spacing: <n> 단계
- Components: <n> 컴포넌트

### ✔️ 자체 검증 통과
- [x] Frontmatter `---` 유효
- [x] 필수 토큰 존재 (primary)
- [x] 8 섹션 순서 준수
- [x] 토큰 참조 무결성
- [x] WCAG AA 대비

### 🔍 다음 단계
\`\`\`bash
npx @google/design.md lint <path>
\`\`\`
```
