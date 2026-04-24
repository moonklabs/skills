---
name: term-sheet-knowledge
description: 텀시트 주요조건, SAFE/전환사채 구조, 캡테이블 희석 계산, Red Flags를 안내합니다. "텀시트 리뷰", "SAFE 설명", "캡테이블 계산", "투자 조건", "밸류에이션 vs 희석" 등으로 실행합니다.
---

# 텀시트 지식 (Term Sheet Knowledge)

**⚠️ 면책 고지**: 이 스킬은 교육 목적으로 텀시트 용어를 설명합니다. 법률 자문을 제공하지 않습니다. 모든 투자 계약은 스타트업 전문 변호사의 검토를 받아야 합니다.

텀시트 주요조건, SAFE/전환사채 구조, 캡테이블 희석 계산, 협상 전략, Red Flags를 제공합니다.

## 작동 방식

```
┌─────────────────────────────────────────────────────────────────┐
│                  TERM SHEET KNOWLEDGE                            │
├─────────────────────────────────────────────────────────────────┤
│  제공하는 정보                                                    │
│  ✓ 텀시트 주요조건 해설 (15개 핵심 조항)                         │
│  ✓ SAFE vs 전환사채 vs Equity 비교                              │
│  ✓ 캡테이블 희석 계산 (라운드별 시뮬레이션)                      │
│  ✓ 협상 포인트 & 우선순위                                        │
│  ✓ Red Flags (피해야 할 조건)                                    │
└─────────────────────────────────────────────────────────────────┘
```

---

## 텀시트 주요조건 (Key Terms)

### 1. 밸류에이션 (Valuation)

**Pre-money vs Post-money**

```
Pre-money: 투자 전 회사 가치
Post-money: 투자 후 회사 가치

Post-money = Pre-money + 투자 금액

예시:
- Pre-money: $8M
- 투자 금액: $2M
- Post-money: $10M
- 투자자 지분: $2M / $10M = 20%
```

**협상 포인트:**
- Pre-money가 높을수록 → 희석율 낮음
- 하지만 다음 라운드에서 "down round" 리스크
- 적정 밸류에이션 > 과도한 밸류에이션

---

### 2. 투자 금액 & 희석율

```
투자자 지분(%) = 투자 금액 / Post-money 밸류에이션

예시:
- Pre-money: $8M
- 투자: $2M
- Post-money: $10M
- 희석율: 20%

창업자 기존 지분 80% → 투자 후 64% (80% × 80%)
```

**희석율 벤치마크:**
- Pre-seed: 10-20%
- Seed: 15-25%
- Series A: 20-30%
- Series B: 15-25%

**Red Flag:**
- 단일 라운드 희석 > 30%
- 누적 희석으로 창업자 지분 < 50% (Series A 전)

---

### 3. 청산우선권 (Liquidation Preference)

**정의:** Exit 시 투자자가 먼저 회수하는 금액

**유형:**

**1x 비참여 (Non-Participating)**
```
Exit $20M, 투자 $2M (20% 지분):
- 투자자 선택:
  Option A: $2M (1x 우선권)
  Option B: $4M (20% 지분)
→ 투자자: $4M 선택
→ 창업자: $16M
```

**1x 참여 (Participating)**
```
Exit $20M, 투자 $2M (20% 지분):
- 투자자:
  Step 1: $2M (1x 우선권)
  Step 2: ($20M - $2M) × 20% = $3.6M
→ 투자자: $5.6M
→ 창업자: $14.4M
```

**2x 비참여**
```
Exit $20M, 투자 $2M (20% 지분):
- 투자자 선택:
  Option A: $4M (2x 우선권)
  Option B: $4M (20% 지분)
→ 투자자: $4M
→ 창업자: $16M
```

**Red Flag:**
- Participating (이중 혜택)
- 2x 이상 Multiple
- Seed/Series A에서 Participating은 비정상

**협상:**
- 1x 비참여가 표준
- Participating이면 강하게 반대
- Cap 설정 (예: 1x Participating with 2x cap)

---

### 4. 희석방지 조항 (Anti-Dilution)

**정의:** Down round 시 투자자 보호

**유형:**

**Full Ratchet (가장 불리)**
```
Original: $10M 밸류, $1/주, 100만주
Down round: $5M 밸류, $0.50/주

Full Ratchet → 투자자 주식을 $0.50 가격으로 조정
→ 투자자 주식 2배, 창업자 대폭 희석
```

**Weighted Average (표준)**
```
Broad-based: 모든 발행주식 기준 (창업자 유리)
Narrow-based: 우선주만 기준 (투자자 유리)

Broad-based가 업계 표준
```

**Red Flag:**
- Full Ratchet (절대 피해야 함)
- Narrow-based (가능하면 피하기)

**협상:**
- Broad-based weighted average 요구
- Pre-seed/Seed는 없는 것도 가능

---

### 5. 보드 구성 (Board Composition)

**전형적 구조:**

**Seed:**
```
Total: 3석
- 창업자: 2석
- 투자자: 1석
```

**Series A:**
```
Total: 5석
- 창업자: 2석
- 투자자: 2석 (Seed 1 + Series A 1)
- 독립: 1석 (mutual agreement)
```

**Series B:**
```
Total: 7석
- 창업자: 2석
- 투자자: 3석
- 독립: 2석
```

**Red Flag:**
- 투자자 과반수 (창업자 통제력 상실)
- 독립이사 선정권이 투자자에게만

**협상:**
- 창업자 + 독립 ≥ 투자자
- 독립이사 선정은 mutual consent

---

### 6. 보호조항 (Protective Provisions)

**정의:** 특정 사항에 투자자 동의 필요

**표준 항목:**
- 신규 투자 유치
- M&A, 청산
- 정관 변경
- 신규 보드 멤버 추가
- 우선주 조건 변경

**Red Flag:**
- 과도한 항목 (예: 임원 채용, 예산 승인)
- 단일 투자자 Veto 권한

**협상:**
- "Major Investor" 기준 명시 (예: 지분 10% 이상)
- 과반수 우선주 동의 (단일 투자자 아님)

---

### 7. 전환권 (Conversion Rights)

**정의:** 우선주 → 보통주 전환

**자동 전환 (Automatic Conversion):**
```
IPO 시 자동 전환
조건:
- 공모가 > $X (예: $50M 밸류에이션)
- 조달 > $Y (예: $10M)
```

**선택 전환 (Optional Conversion):**
투자자가 언제든지 선택 가능

**Red Flag:**
- 자동 전환 조건이 너무 높음
- 투자자만 선택 전환 가능 (창업자는 불가)

---

### 8. 상환권 (Redemption Rights)

**정의:** 투자자가 회사에 주식 되팔기 요구

**Red Flag:**
- Seed/Series A에 상환권 (비정상)
- 상환 시기가 너무 이름 (예: 3년)

**협상:**
- 상환권 삭제 요구
- 최소 기간 5년 이상

---

### 9. 배당 (Dividends)

**유형:**

**누적 배당 (Cumulative):**
```
매년 X% 누적, Exit 시 지급
→ 실질적 이자 (투자자 유리)
```

**비누적 배당 (Non-Cumulative):**
```
이사회 결정 시에만 지급
→ 스타트업에서 거의 지급 안 함
```

**Red Flag:**
- 누적 배당 (피해야 함)
- 배당률 > 8%

**협상:**
- 배당 삭제 또는 비누적 배당

---

### 10. 창업자 지분귀속 (Founder Vesting)

**표준 구조:**
```
4년 Vesting, 1년 Cliff

예시:
- Year 0: 0%
- Year 1 (Cliff): 25%
- Year 2: 50%
- Year 3: 75%
- Year 4: 100%

월별 Vesting (Year 1 이후): 1/48씩
```

**Single Trigger vs Double Trigger:**

**Single Trigger:**
```
M&A 시 즉시 100% Vesting
→ 창업자 유리
```

**Double Trigger:**
```
M&A + 해고 → 100% Vesting
→ 인수자 유리 (창업자 유지 가능)
```

**협상:**
- Single Trigger 요구 (초기 라운드)
- Double Trigger 수용 가능 (후기 라운드)
- Acceleration 범위 (50% vs 100%)

---

### 11. 우선매수권 & 동반매도권

**우선매수권 (Right of First Refusal, ROFR):**
```
창업자 주식 매도 시 투자자에게 우선 기회
→ 표준 조항, 수용 가능
```

**동반매도권 (Co-Sale / Tag-Along):**
```
창업자 주식 매도 시 투자자도 동일 조건으로 매도 가능
→ 표준 조항
```

**동반매도요구권 (Drag-Along):**
```
투자자 과반 동의 시 모든 주주 강제 매도
→ M&A 용이하게
→ 표준 조항, 수용 가능
```

---

### 12. 우선인수권 (Pro-Rata Rights)

**정의:** 다음 라운드에서 지분율 유지 위해 참여 권리

**협상:**
- Major Investor에게만 부여
- 초과 할당 (over-allotment) 제한

---

### 13. 정보 제공 (Information Rights)

**표준:**
- 월간 재무제표
- 연간 감사 재무제표
- 연간 예산
- 이사회 자료 (옵저버 권한)

**Red Flag:**
- 과도한 정보 요구 (예: 주간 보고)
- 경쟁사일 수 있는 투자자에게 민감 정보

---

### 14. 비용 부담 (No-Shop & Expenses)

**No-Shop:**
```
텀시트 서명 후 30-60일간 다른 투자자와 협상 금지
→ 표준 조항, 수용 가능
```

**Expenses:**
```
투자자 변호사 비용을 회사가 부담
→ 상한선 설정 ($10K-$25K)
```

---

### 15. 옵션 풀 (Employee Option Pool)

**Pre-money vs Post-money:**

**Pre-money Pool (투자자 유리):**
```
Pre-money: $8M
옵션 풀: 15% (Pre-money 기준)
→ 옵션 풀이 창업자 희석

실제 계산:
- 창업자: 80% × (1 - 15%) = 68%
- 옵션 풀: 15%
- 투자자: 20% (post-money 기준)
→ 창업자만 희석
```

**Post-money Pool (창업자 유리):**
```
Post-money: $10M
옵션 풀: 15% (Post-money 기준)
→ 창업자·투자자 함께 희석
```

**협상:**
- Post-money 옵션 풀 요구
- 필요한 만큼만 (과도한 풀 피하기)

---

## SAFE (Simple Agreement for Future Equity)

### SAFE 구조

**기본 원리:**
```
현재 투자 → 다음 Equity 라운드에서 주식 전환
밸류에이션 없이 투자 (현재 협상 회피)
```

**4가지 유형:**

**1. Valuation Cap (가장 일반적)**
```
Cap: $5M
다음 라운드: $10M pre-money
→ SAFE 투자자는 $5M 기준 전환 (2배 유리)
```

**2. Discount (단독 또는 Cap + Discount)**
```
Discount: 20%
다음 라운드: $1/주
→ SAFE 투자자는 $0.80/주 전환
```

**3. Valuation Cap + Discount**
```
두 가지 중 유리한 것 선택
```

**4. MFN (Most Favored Nation)**
```
다음 SAFE보다 불리하지 않음
→ 초기 투자자 보호
```

### SAFE 희석 계산

```
예시:
- SAFE 투자: $500K, Cap $5M
- Series A: $2M at $10M pre-money

SAFE 전환:
- SAFE Cap $5M 기준 → 지분 10% ($500K / $5M)
- Series A $10M pre-money 기준 → 20% ($2M / $10M)

Post-money:
- $10M + $2M + SAFE 희석 조정 = $12M+
- 창업자: ~66%
- SAFE: ~10%
- Series A: ~20%
- 옵션 풀: ~4%
```

### SAFE vs Equity

| 항목 | SAFE | Equity |
|------|------|--------|
| 밸류에이션 | 미정 (Cap만) | 확정 |
| 협상 | 간단 (2주) | 복잡 (2개월) |
| 비용 | 낮음 ($2K) | 높음 ($20K+) |
| 투자자 권리 | 없음 | 보드, 보호조항 |
| 전환 | 다음 라운드 | 즉시 |
| 적합 단계 | Pre-seed | Seed+ |

**SAFE의 장점:**
- 빠름, 저렴함
- 밸류에이션 협상 연기
- 표준 문서 (YC SAFE)

**SAFE의 단점:**
- 캡테이블 복잡 (여러 SAFE 겹침)
- 다음 라운드까지 희석 불확실
- 투자자 권리 없음 (보드, 정보권)

---

## 전환사채 (Convertible Note)

### 구조

```
채권 (Debt) → 다음 라운드에서 주식 전환

주요 조건:
- 원금 (Principal)
- 이자율 (Interest Rate): 5-8%
- 만기 (Maturity): 18-24개월
- 전환 Discount: 15-25%
- Valuation Cap: 선택
```

### SAFE vs 전환사채

| 항목 | SAFE | 전환사채 |
|------|------|----------|
| 법적 성격 | 계약 | 채권 |
| 이자 | 없음 | 5-8% |
| 만기 | 없음 | 18-24개월 |
| 상환 의무 | 없음 | 만기 시 상환 또는 전환 |
| 복잡도 | 낮음 | 중간 |

**선호도:**
- 미국: SAFE 선호 (간단)
- 한국/아시아: 전환사채 선호 (법적 확립)

---

## 캡테이블 & 희석 계산

### 초기 캡테이블

```
창업:
- 창업자 A: 60% (6M주)
- 창업자 B: 40% (4M주)
Total: 10M주 (Fully Diluted)
```

### Pre-seed (SAFE)

```
SAFE 투자: $500K at $5M Cap

가정: Series A에서 전환
현재 캡테이블 변화 없음
```

### Seed Round

```
투자: $2M at $8M pre-money
옵션 풀: 10% (pre-money)
Post-money: $10M

희석 계산:
1. 옵션 풀 만들기 (pre-money)
   - 기존: 10M주
   - 옵션: 1.11M주 (10% / 90%)
   - Total: 11.11M주

2. 투자자 주식
   - 투자자 지분: 20% (post-money)
   - 투자자 주식: 2.78M주 (20% / 80%)
   - Total: 13.89M주

캡테이블 (Seed 후):
- 창업자 A: 54% (6M / 11.11M × 80%)
- 창업자 B: 36% (4M / 11.11M × 80%)
- 옵션 풀: 8% (1.11M / 13.89M)
- Seed 투자자: 20% (2.78M / 13.89M)
- SAFE: 아직 전환 안 됨
```

### Series A

```
투자: $5M at $20M pre-money
옵션 풀: 15% (post-money)

SAFE 전환:
- SAFE $500K at $5M Cap
- $500K / $5M = 10% (Cap 기준)
- 하지만 Pre-money $20M → 조정 필요
- SAFE 주식 ≈ 2.5% (post-money)

Series A 주식:
- 투자: $5M
- Post-money: $25M (pre $20M + $5M)
- 지분: 20%

캡테이블 (Series A 후):
- 창업자 A: 37.8%
- 창업자 B: 25.2%
- 옵션 풀: 15%
- SAFE: 2.5%
- Seed: 14%
- Series A: 20%
```

### 희석 시뮬레이터

```
스프레드시트 템플릿:
https://captable.io
https://carta.com

주요 변수:
- 투자 금액
- Pre-money 밸류에이션
- 옵션 풀 크기
- SAFE Cap & Discount
```

---

## 협상 전략

### 우선순위

**Must-Have (비협상):**
1. 1x 비참여 청산우선권
2. Broad-based weighted average 희석방지
3. 창업자 보드 통제 또는 동등
4. Post-money 옵션 풀

**Important:**
5. Single Trigger Acceleration
6. 투자자 권리 범위 제한
7. No-Shop 기간 최소화
8. 비용 상한

**Nice-to-Have:**
9. 배당 삭제
10. 상환권 삭제

### 협상 팁

**1. 변호사 필수**
```
스타트업 전문 변호사 선임
비용: $10K-$25K (worth it)
```

**2. 표준 문서 사용**
```
NVCA 표준 문서
YC SAFE
→ 비표준 조항 의심
```

**3. 여러 텀시트 비교**
```
최소 2-3개 텀시트 받기
조건 비교표 작성
밸류에이션만 보지 말고 전체 조건
```

**4. 레퍼런스 체크**
```
투자자의 포트폴리오 CEO에게 문의
- 보드 참여 적극성
- 어려울 때 지원
- 후속 투자 여부
```

---

## Red Flags (피해야 할 조건)

### 🚩 Participating 청산우선권

```
이중 혜택 (우선권 + 지분)
→ Exit에서 창업자 불리
→ Seed/A에서는 절대 안 됨
```

### 🚩 Full Ratchet 희석방지

```
Down round 시 창업자 대폭 희석
→ "Death spiral"
→ 절대 수용 불가
```

### 🚩 투자자 보드 과반수

```
창업자 통제력 상실
→ 해고 가능
→ 전략 결정권 없음
```

### 🚩 과도한 보호조항

```
일상 운영까지 투자자 동의 필요
→ 의사결정 마비
→ 범위 제한 필수
```

### 🚩 개인 보증

```
창업자 개인 자산 담보
→ 스타트업에서는 비정상
→ 거부
```

---

## 한국 특화: 전환사채 & 주식인수계약

### 한국 전환사채 구조

```
일반적 조건:
- 전환가격: 발행가 대비 Discount (20-30%)
- 전환청구기간: 1년 후 ~ 만기 전
- 만기: 3년
- 이자율: 0-3%
- 조기상환: 일부 허용
```

### 주식인수계약 (SPA)

```
한국에서 더 일반적 (미국의 Stock Purchase Agreement)

주요 조항:
- 주식 발행가액
- 진술 및 보증 (Representations & Warranties)
- 계약 전 조건 (Conditions Precedent)
- 손해배상 책임
```

---

## 관련 스킬 및 커맨드

- **financial-modeling** — 희석 시뮬레이션, 캡테이블 모델링
- **fundraising-process** — 텀시트는 Week 7에 수령
- `/fundraise-pipeline` — 여러 텀시트 비교 분석
- `/dd-prep` — DD 단계에서 텀시트 협상 준비
