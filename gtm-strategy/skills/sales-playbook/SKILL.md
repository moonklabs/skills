---
name: sales-playbook
description: B2B 세일즈 프로세스와 방법론을 안내합니다 — MEDDPICC, 세일즈 단계, 팀 설계. "세일즈", "영업", "딜", "MEDDPICC", "세일즈 프로세스" 등으로 실행합니다.
---

# Sales Playbook

> 익숙하지 않은 플레이스홀더가 보이거나 연결된 도구를 확인하려면 [CONNECTORS.md](../../CONNECTORS.md)를 참조하세요.

B2B 세일즈 플레이북입니다. MEDDPICC 방법론, Discovery → Close 5단계 프로세스, 핵심 지표, 팀 설계를 통해 반복 가능하고 예측 가능한 세일즈 엔진을 구축합니다.

## 작동 방식

```
┌─────────────────────────────────────────────────────────────────┐
│                      SALES PLAYBOOK FRAMEWORK                    │
├─────────────────────────────────────────────────────────────────┤
│  기본 기능 (단독 작동)                                            │
│  ✓ MEDDPICC 7가지 Qualification 기준                            │
│  ✓ Discovery → Demo → Proposal → Negotiation → Close 5단계     │
│  ✓ 세일즈 지표 벤치마크 (Win Rate, Sales Cycle, ACV)             │
│  ✓ 세일즈 팀 설계 (SDR/BDR, AE, CSM 역할)                        │
├─────────────────────────────────────────────────────────────────┤
│  강화 모드 (도구 연결 시)                                         │
│  + ~~CRM: 파이프라인 분석, Win/Loss 패턴                         │
│  + ~~calendar: 미팅 스케줄링, Sales Cycle 추적                  │
│  + ~~email: 아웃리치 시퀀스, 팔로업 자동화                       │
└─────────────────────────────────────────────────────────────────┘
```

## 시작하기

1. **Qualification**: "MEDDPICC로 딜을 검증해줘"
2. **세일즈 프로세스**: "Discovery 미팅 준비를 도와줘"
3. **팀 설계**: "세일즈 팀을 어떻게 구성해야 해?"
4. **지표 추적**: "우리 Win Rate가 정상인지 알려줘"

## 세일즈 철학

### 핵심 원칙

1. **문제 해결자, 제품 파는 사람 아님**
   - "우리 제품이 최고"가 아니라
   - "당신 문제를 이렇게 풀어드릴게요"

2. **결과 판매, 기능 판매 아님**
   - "AI 기능 탑재"가 아니라
   - "영업 생산성 30% 향상"

3. **반복 가능한 프로세스**
   - 운 아닌 시스템
   - 1등 세일즈를 표준화

4. **정확한 예측**
   - "희망적 파이프라인" 아닌
   - "데이터 기반 Forecast"

---

## MEDDPICC 방법론

### 개요

**MEDDPICC**: 7가지 Qualification 기준. 모두 충족 시 Win Rate 70%+

```
M - Metrics (측정 지표)
E - Economic Buyer (최종 결정권자)
D - Decision Criteria (의사결정 기준)
D - Decision Process (의사결정 프로세스)
P - Identify Pain (통증 식별)
C - Champion (내부 전도사)
C - Competition (경쟁)
```

### M - Metrics (측정 지표)

**정의**: 고객이 달성하고 싶은 정량적 목표

**질문**:
- "현재 [지표]가 어떻게 되나요?"
- "목표는?"
- "이 차이가 비즈니스에 어떤 영향?"

**예시**:
- 현재: 영업팀 월 100건 Deal, Win Rate 15%
- 목표: 월 200건, Win Rate 25%
- 영향: 매출 3x 증가 (₩10억 → ₩30억)

**문서화**:
```markdown
## Metrics
- Current: 100 deals/mo, 15% win rate
- Goal: 200 deals/mo, 25% win rate
- Impact: ₩20B additional revenue/year
- Timeline: Achieve within 6 months
```

**Red Flag**:
- ❌ 정량 목표 없음 ("그냥 더 나아지면")
- ❌ 모호한 목표 ("효율성 향상")
- ❌ 측정 불가능 ("느낌적으로 개선")

### E - Economic Buyer (최종 결정권자)

**정의**: 예산 승인권자. 최종 Yes/No

**질문**:
- "이 프로젝트 예산 승인은 누가 하나요?"
- "CFO도 관여하나요?"
- "구매 승인 프로세스는?"

**레벨 파악**:
| 역할 | 권한 | 예산 범위 | 접촉 방법 |
|------|------|-----------|-----------|
| **End User** | 사용 | $0 | 초기 접촉 |
| **Manager** | 추천 | <$10K | Influencer |
| **Director** | 승인 | $10-100K | Champion 후보 |
| **VP/C-level** | 최종 결정 | $100K+ | Executive 브리핑 |

**예시**:
- SMB: CEO (직접 결정)
- Mid-Market: VP Sales (CFO 승인 필요)
- Enterprise: CIO + CFO + Procurement

**전략**:
- **Multi-threading**: 여러 레벨 동시 접촉
- **Executive Alignment**: 조기에 EB와 접촉
- **Champion 활용**: EB 미팅 세팅 도와달라

**Red Flag**:
- ❌ EB를 만난 적 없음
- ❌ "우리 팀장이 결정해요" (실제는 CFO)
- ❌ EB가 관심 없음

### D - Decision Criteria (의사결정 기준)

**정의**: 구매 결정 시 평가하는 기준

**질문**:
- "솔루션 선정 기준은 무엇인가요?"
- "각 기준의 가중치는?"
- "Must-have vs Nice-to-have는?"

**일반적 기준**:
1. **기능 적합성** (30%)
2. **가격** (25%)
3. **통합 용이성** (15%)
4. **벤더 신뢰성** (15%)
5. **고객 지원** (10%)
6. **구현 시간** (5%)

**전략**:
- **우리 강점 강조**: 기준에 우리 장점 포함시키기
  - 예: "AI 자동화 기능이 중요하지 않나요?"
- **경쟁사 약점**: 그들이 못하는 것을 기준에

**문서화**:
```markdown
## Decision Criteria
1. Feature fit (30%) - ✅ Strong
2. Price (25%) - 🟡 Medium (higher than X)
3. Integration (15%) - ✅ Strong (native Salesforce)
4. Vendor stability (15%) - 🟡 Startup risk
5. Support (10%) - ✅ Strong (Korean 24/7)
6. Implementation (5%) - ✅ Strong (2 weeks)

Overall: Strong (4/6 green)
```

### D - Decision Process (의사결정 프로세스)

**정의**: 구매 승인까지 단계 및 타임라인

**질문**:
- "구매 프로세스는 어떻게 되나요?"
- "각 단계별 소요 시간은?"
- "누가 관여하나요?"

**전형적 프로세스**:
```
1. Requirements Gathering (2주)
   - End Users, Manager
2. Vendor Evaluation (4주)
   - Demo, POC
   - Manager, Director
3. Pricing & Negotiation (2주)
   - Procurement, CFO
4. Legal Review (2주)
   - Legal, Security
5. Final Approval (1주)
   - C-level
6. Procurement (1주)
   - PO 발행

Total: 12주 (3개월)
```

**주의사항**:
- **숨겨진 단계**: Legal, Security, Procurement
- **여름/연말**: 의사결정 지연 (휴가, 예산 마감)
- **갑작스런 중단**: 우선순위 변경, 예산 동결

**전략**:
- **역산 계획**: Close 목표일 - 12주 = 시작일
- **Milestone 트래킹**: 각 단계 완료 확인
- **블로커 조기 해결**: Legal 이슈 미리 파악

### P - Identify Pain (통증 식별)

**정의**: 고객이 해결하려는 핵심 Pain Point

**Pain의 깊이** (3 Levels):
1. **표면 Pain** (Symptom): "CRM 사용이 불편해요"
2. **근본 Pain** (Root Cause): "영업팀이 데이터 입력 안 함"
3. **비즈니스 영향** (Impact): "정확한 Forecast 불가 → CFO 불만"

**질문 (3 Why's)**:
1. "어떤 문제가 있나요?" → "CRM 사용 불편"
2. "왜 불편한가요?" → "복잡해서 입력 안 함"
3. "입력 안 하면 무슨 일이?" → "Forecast 틀림 → 투자 계획 차질"

**Pain 강도 측정**:
- **Critical**: 지금 당장 해결 안 하면 사업 위험
- **High**: 3개월 내 해결 필요
- **Medium**: 6개월 내
- **Low**: 언젠가 (구매 안 함)

**예시**:
```markdown
## Pain Points
1. **Critical**: Inaccurate forecast
   - Root: No CRM data entry
   - Impact: CFO can't plan hiring/investment
   - Cost: Missed $2M revenue target last Q

2. **High**: Low win rate (15% vs 25% industry)
   - Root: No lead scoring
   - Impact: Sales waste time on bad leads
   - Cost: 50% sales time wasted = $500K/yr
```

**Red Flag**:
- ❌ Pain이 약함 ("좀 더 나으면 좋겠어요")
- ❌ 비용 산정 안 됨 (얼마 손해인지 모름)
- ❌ 대안 존재 (Excel로도 가능)

### C - Champion (내부 전도사)

**정의**: 내부에서 우리 솔루션 옹호하는 사람

**특징**:
- 우리 성공이 본인 이익 (승진, KPI)
- 내부 정치 파악
- EB 접근 도움
- 경쟁사 대응 정보 제공

**Champion 식별**:
- "우리 이기면 당신에게 어떤 이익?"
- "내부 반대 의견은?"
- "우리가 어떻게 도울까요?"

**Champion vs Seller**:
| Champion | Seller (담당자) |
|----------|-----------------|
| 적극 추진 | 정보만 수집 |
| 정치 파악 | 중립 |
| EB 연결 | 보고만 |
| 위험 감수 | 안전 선호 |

**Champion 키우기**:
- **ROI 계산 제공**: 그들이 상사 설득할 자료
- **Internal Deck**: "내부용 발표 자료 드릴게요"
- **Success Story**: 유사 회사 사례
- **Executive 브리핑**: EB 미팅 함께 준비

**Red Flag**:
- ❌ Champion 없음
- ❌ Champion이 영향력 없음 (인턴)
- ❌ Champion이 우리 안 믿음

### C - Competition (경쟁)

**정의**: 우리와 비교 중인 대안

**경쟁 유형**:
1. **Direct**: 같은 카테고리 (Salesforce, HubSpot)
2. **Indirect**: 다른 방식 (Excel, 자체 개발)
3. **Status Quo**: 아무것도 안 함

**질문**:
- "다른 솔루션도 보고 계신가요?"
- "현재 어떤 방식 쓰시나요?"
- "각 옵션의 장단점은?"

**경쟁사 분석**:
```markdown
## Competition
- **Vendor A**: Market leader, expensive
  - Strength: Brand, features
  - Weakness: $300/user (3x our price)
  - Our Counter: "Same core value, 1/3 price"

- **Status Quo (Excel)**: Free
  - Strength: No cost
  - Weakness: Manual, error-prone
  - Our Counter: "ROI: 500h saved = $50K/year"
```

**전략**:
- **배틀카드 활용**: competitive-landscape 스킬 참조
- **FUD 피하기**: 경쟁사 깎아내리기 X
- **차별화**: "우리만의 독특한 가치"

---

## 세일즈 5단계 프로세스

### 단계 개요

```
Discovery → Demo → Proposal → Negotiation → Close
  (20%)     (30%)    (50%)       (70%)        (95%)
```

(괄호 = Close 확률)

### 1. Discovery (발견)

**목표**: MEDDPICC 7가지 파악

**소요 시간**: 1-2 미팅 (60-90분 each)

**준비**:
- [ ] 고객 웹사이트, LinkedIn 리서치
- [ ] 경쟁사 사용 여부 파악
- [ ] 산업 트렌드 파악

**미팅 구조** (60분):
1. **Rapport (5분)**: 관계 형성
2. **Agenda Setting (2분)**: 오늘 목표 설정
3. **Current State (15분)**: 현재 문제
4. **Future State (15분)**: 이상적 상태
5. **Impact (10분)**: Gap의 비용
6. **Decision Process (10분)**: 구매 프로세스
7. **Next Steps (3분)**: 다음 미팅 확정

**핵심 질문**:
- "현재 [프로세스]는 어떻게 하시나요?"
- "가장 큰 Pain Point는?"
- "이상적으로는 어떻게 되길 원하나요?"
- "이 문제 안 풀면 무슨 일이?"
- "구매 결정은 누가, 언제, 어떻게?"

**성공 기준**:
- [ ] MEDDPICC 7개 중 5개 이상 파악
- [ ] Champion 후보 식별
- [ ] Next Step 확정 (Demo 날짜)

### 2. Demo (데모)

**목표**: 솔루션이 Pain 해결함을 증명

**소요 시간**: 1 미팅 (45-60분)

**준비**:
- [ ] Discovery 노트 리뷰
- [ ] 고객 Pain에 맞춘 데모 시나리오
- [ ] 고객 데이터로 데모 (Mock Data)

**데모 구조** (45분):
1. **Recap (5분)**: Discovery 요약
2. **Demo (25분)**: 시나리오 기반
3. **Q&A (10분)**: 질문 응대
4. **Next Steps (5분)**: Proposal 논의

**데모 원칙**:
- **Show, Don't Tell**: 말 대신 시연
- **Customer Story**: "A사는 이렇게 써서 30% 증대"
- **Pain → Solution**: Discovery Pain 직접 해결
- **Hands-on**: 고객이 직접 클릭

**안티패턴**:
- ❌ Feature Dump (모든 기능 나열)
- ❌ Generic Demo (맞춤화 X)
- ❌ 45분 내내 말만

**성공 기준**:
- [ ] "Aha moment" 확인 ("오, 이거 좋네요!")
- [ ] 기술적 질문 (관심 신호)
- [ ] Champion이 EB에게 공유하겠다고
- [ ] Proposal 미팅 확정

### 3. Proposal (제안)

**목표**: 가격, 범위, 타임라인 제시

**소요 시간**: 1 미팅 (60분) + 문서 작성

**Proposal 구조**:
```markdown
# [고객사] 제안서

## Executive Summary (1페이지)
- Problem, Solution, Value (ROI)

## Scope of Work (1페이지)
- Included features
- Implementation timeline
- Training & Support

## Pricing (1페이지)
- 3-tier options (Good/Better/Best)
- Annual discount (15-20%)

## Case Study (1페이지)
- 유사 고객 성공 사례

## Next Steps (1페이지)
- Decision timeline
- Contract & Onboarding
```

**가격 제시**:
- **3 옵션**: Anchor (높음), Target (중간), Entry (낮음)
- **Annual 강조**: "20% 절약"
- **ROI 계산**: "12개월 안에 투자 회수"

**미팅**:
1. **Proposal Walkthrough (20분)**: 문서 설명
2. **Questions (20분)**: 우려 사항 해소
3. **Objection Handling (15분)**: 가격, 경쟁사
4. **Closing (5분)**: "진행하시겠어요?"

**성공 기준**:
- [ ] 가격에 대한 합의 (범위 내)
- [ ] Legal/Procurement 다음 단계
- [ ] Champion이 EB 설득 중

### 4. Negotiation (협상)

**목표**: 조건 합의, 계약 준비

**소요 시간**: 1-3주 (이메일 왕래)

**협상 포인트**:
| 고객 요청 | 우리 대응 | 조건 |
|-----------|-----------|------|
| 가격 할인 | 5-10% 가능 | Annual 약정 |
| 구현 지원 | 무료 온보딩 | Reference 고객 동의 |
| Custom 기능 | 로드맵 우선순위 | $X 추가 비용 |
| 긴 결제 조건 | Net 60 허용 | 계약 3년 |

**협상 원칙**:
1. **Give to Get**: 무료 양보 X, 항상 교환
2. **Anchor High**: 첫 제안은 높게
3. **Silence**: 고객이 먼저 말하게
4. **Walk-away**: 최소 수락 금액 설정

**Legal 리뷰**:
- **MSA** (Master Service Agreement)
- **SLA** (Service Level Agreement)
- **DPA** (Data Processing Agreement)

**성공 기준**:
- [ ] 최종 가격 합의
- [ ] Legal 승인
- [ ] PO (Purchase Order) 발행 예정일

### 5. Close (클로징)

**목표**: 계약 서명, 킥오프

**소요 시간**: 1주

**체크리스트**:
- [ ] Contract 서명 (DocuSign)
- [ ] PO 수령
- [ ] Payment (선납 or Net 30)
- [ ] Kickoff 미팅 예약
- [ ] CSM 배정
- [ ] CRM에 Won 기록

**Kickoff 미팅**:
- Implementation 타임라인
- 담당자 소개 (AE → CSM 핸드오프)
- 첫 30일 목표 설정

**Win 분석**:
```markdown
## Win Analysis: [고객사]
- Deal Size: $[금액]
- Sales Cycle: [X]일
- Win Reason:
  1. [이유 1] (40%)
  2. [이유 2] (35%)
  3. [이유 3] (25%)
- Lesson: [배운 점]
```

---

## 핵심 세일즈 지표

### Win Rate (영업 성공률)

**정의**: Won Deals / Total Opportunities

**벤치마크**:
| 고객 유형 | Win Rate | 비고 |
|-----------|----------|------|
| **SMB** | 20-30% | 빠른 결정, 낮은 ACV |
| **Mid-Market** | 25-35% | 복잡도 중간 |
| **Enterprise** | 30-40% | 긴 주기, 높은 ACV |

**개선 전략**:
- ICP 정제 (승률 높은 세그먼트 집중)
- MEDDPICC 엄격 적용
- 배틀카드 업데이트

### Sales Cycle (영업 주기)

**정의**: Opportunity Created → Close 평균 일수

**벤치마크**:
| 고객 유형 | Sales Cycle | 비고 |
|-----------|-------------|------|
| **SMB** | 30-60일 | Self-serve 가능하면 < 30일 |
| **Mid-Market** | 60-120일 | Procurement 개입 |
| **Enterprise** | 120-270일 | Legal, Security, 다수 의사결정자 |

**단축 전략**:
- Discovery 철저 (뒤늦은 Red Flag 방지)
- EB 조기 접촉
- Legal 템플릿 사전 준비

### ACV (Average Contract Value)

**정의**: 계약 연간 가치

**벤치마크**:
| 세그먼트 | ACV | 비고 |
|----------|-----|------|
| **SMB** | $5K-$25K | 신속 결정 |
| **Mid-Market** | $25K-$100K | Sweet Spot |
| **Enterprise** | $100K+ | 복잡, 높은 마진 |

**최적화**:
- Upsell (더 높은 Tier)
- Multi-year (3년 계약)
- Add-ons (추가 모듈)

### Pipeline Coverage

**정의**: Total Pipeline / Quarterly Quota

**목표**: **3-5x**

**예시**:
```
분기 목표: $500K
Pipeline: $2M
Coverage: 4x ✅
```

**부족 시 (<3x)**:
- 신규 리드 생성 가속
- SDR 채용
- 마케팅 캠페인 확대

### Conversion Rates (단계별 전환율)

**파이프라인 퍼널**:
```
Lead (100%)
  ↓ 10-20%
Opportunity (SQL)
  ↓ 30-50%
Demo
  ↓ 50-70%
Proposal
  ↓ 60-80%
Negotiation
  ↓ 80-90%
Close
```

**최적화**:
- 병목 단계 식별
- A/B 테스트 (Pitch, Demo Script)
- 교육 강화

---

## 세일즈 팀 설계

### 역할 정의

#### SDR/BDR (Sales/Business Development Rep)

**책임**: Lead 생성 및 Qualification

**활동**:
- Cold Outreach (이메일, LinkedIn)
- Inbound Lead 응대
- BANT Qualification (Budget, Authority, Need, Timeline)
- AE에게 패스

**지표**:
- SQL (Sales Qualified Lead): 월 20-30개
- Conversion (Lead → SQL): 10-20%
- Activity: 일 50-100 Touch

**보상**:
- Base: ₩3,000만 + Variable: ₩1,500만
- SQL당 인센티브

#### AE (Account Executive)

**책임**: Opportunity → Close

**활동**:
- Discovery, Demo, Proposal
- MEDDPICC 실행
- 계약 협상

**지표**:
- Quota: 분기 $200-500K (경력별)
- Win Rate: 25-35%
- Sales Cycle: 60-90일

**보상**:
- Base: ₩6,000만 + Commission: ₩6,000만 (100% quota 달성 시)
- OTE (On-Target Earnings): ₩12,000만

#### CSM (Customer Success Manager)

**책임**: 고객 온보딩, 유지, 확장

**활동**:
- Onboarding (첫 30일)
- Quarterly Business Review (QBR)
- Renewal 관리
- Upsell/Cross-sell

**지표**:
- NRR (Net Revenue Retention): >110%
- Gross Churn: <10%/년
- Upsell: 신규 ARR의 30%

**보상**:
- Base: ₩5,000만 + Variable: ₩2,000만
- NRR, Renewal 기반

### 팀 구조 (단계별)

**Seed ($0-1M ARR)**:
- Founder-led Sales
- 1-2 AE (제너럴리스트)

**Series A ($1-5M ARR)**:
- 1 Sales Lead
- 2-3 AE
- 1 SDR (Inbound)

**Series B ($5-20M ARR)**:
- 1 VP Sales
- 6-8 AE (세그먼트별: SMB, Mid, Ent)
- 3-4 SDR
- 2-3 CSM

### Hiring (채용)

**AE 채용 기준**:
- [ ] 관련 산업 경험 (3+ 년)
- [ ] 유사 ACV 경험 ($25K-100K)
- [ ] MEDDPICC 또는 유사 방법론
- [ ] Hunter Mindset (농부 아닌 사냥꾼)
- [ ] Coachability (가르침 수용)

**면접 프로세스**:
1. **Screen (30분)**: 이력, 동기
2. **Role Play (60분)**: Discovery 시뮬레이션
3. **Case Study (take-home)**: Deal 분석
4. **Team Fit (30분)**: 문화 적합성
5. **Reference Check**: 전 직장 상사

### Onboarding (온보딩)

**Week 1-2: 제품**
- 제품 교육
- Demo 연습 (20회)
- ICP, Persona 이해

**Week 3-4: Shadowing**
- 선배 AE Discovery 참관 (10회)
- Demo 참관 (5회)

**Week 5-6: Reverse Shadowing**
- 본인 Discovery, 선배 참관
- 피드백 및 코칭

**Week 7-8: Solo**
- 독립 Deal 운영
- 첫 Win 목표

**90일 목표**:
- 제품 전문가
- 첫 Deal Close
- Quota의 50% 달성

### Coaching (코칭)

**1-on-1 (주간)**:
- Deal Review (MEDDPICC)
- Pipeline 건강도 체크
- 스킬 향상 (Objection Handling)

**Team Meeting (주간)**:
- Win/Loss 공유
- 베스트 프랙티스
- 경쟁사 업데이트

**Training (월간)**:
- 외부 강사
- 역할극 (Role Play)
- 신규 Feature 교육

---

## 관련 스킬

- **gtm-strategy**: Sales-Led GTM 모션 설계
- **pricing-strategy**: 가격 협상 전략
- **competitive-landscape**: 배틀카드 활용
- **investor-research**: VC 세일즈에 MEDDPICC 응용

## 팁

- **MEDDPICC 엄격 적용**: 7개 중 5개 미만이면 Qualify Out (시간 낭비 방지)
- **Multi-threading**: 1명만 접촉 X, 여러 레벨 동시 관계
- **Champion 필수**: 없으면 Win 확률 <10%
- **Discovery가 80%**: 여기서 이기고 지는게 결정
- **Feature → Value**: "AI 기능"이 아니라 "30% 시간 절약"
- **Objection = 관심**: 질문 많으면 좋은 신호
- **Silence 활용**: 가격 제시 후 침묵, 고객이 먼저 말하게
- **Process > Talent**: 1등 세일즈의 방법을 표준화
- **데이터 추적**: Win/Loss 패턴 분석, 지속 개선
