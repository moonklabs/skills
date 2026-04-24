---
name: pricing-strategy
description: 가격 전략 및 패키징을 안내합니다 — 가격 모델, 밸류 메트릭, 심리학, 패키징. "가격", "요금제", "패키징", "밸류 메트릭", "가격 책정" 등으로 실행합니다.
---

# Pricing Strategy

> 익숙하지 않은 플레이스홀더가 보이거나 연결된 도구를 확인하려면 [CONNECTORS.md](../../CONNECTORS.md)를 참조하세요.

SaaS 가격 전략 프레임워크입니다. 가격 모델 선택, 밸류 메트릭 설정, 심리학 적용, Good/Better/Best 패키징, Feature Fencing을 통해 고객 가치와 매출을 최적화합니다.

## 작동 방식

```
┌─────────────────────────────────────────────────────────────────┐
│                    PRICING STRATEGY FRAMEWORK                    │
├─────────────────────────────────────────────────────────────────┤
│  기본 기능 (단독 작동)                                            │
│  ✓ 비즈니스 모델 기반 가격 모델 추천                              │
│  ✓ 밸류 메트릭 4기준 평가 (설명/정렬/예측/확장)                   │
│  ✓ Good/Better/Best 3-tier 패키징                               │
│  ✓ 가격 심리학 적용 (Anchoring, Decoy, Charm)                   │
├─────────────────────────────────────────────────────────────────┤
│  강화 모드 (도구 연결 시)                                         │
│  + ~~analytics: 고객별 사용량 데이터로 메트릭 검증                │
│  + ~~CRM: 딜별 가격 민감도 및 패키지 선호 분석                    │
│  + ~~spreadsheet: 가격 시나리오별 매출 시뮬레이션                │
└─────────────────────────────────────────────────────────────────┘
```

## 시작하기

1. **가격 모델 선택**: "우리 SaaS에 맞는 가격 모델은?"
2. **밸류 메트릭**: "어떤 단위로 과금해야 해?"
3. **패키징**: "3-tier 요금제를 만들어줘"
4. **가격 최적화**: "현재 가격을 검증해줘"

## 가격 모델 (Pricing Models)

### 5가지 주요 모델

| 모델 | 정의 | 장점 | 단점 | 최적 상황 |
|------|------|------|------|-----------|
| **Per-Seat** | 사용자당 과금 | 예측 가능, 단순 | 팀 확장 저항 | 협업 툴 (Slack) |
| **Usage-Based** | 사용량 과금 | 가치 정렬, 확장성 | 예측 어려움 | API, 인프라 (Twilio) |
| **Flat-Rate** | 고정 요금 | 마찰 없음 | 가치 누수 | 소규모 SaaS |
| **Tiered** | 구간별 과금 | 업셀 기회 | 복잡도 | 범용 SaaS (HubSpot) |
| **Hybrid** | 조합 | 유연성 | 가장 복잡 | Enterprise (Salesforce) |

### 1. Per-Seat (사용자당)

**공식**: `가격 = 사용자 수 × User당 가격`

**예시**:
- Slack: $8/user/월
- Zoom: $15/user/월
- Asana: $10.99/user/월

**장점**:
- ✅ 단순 (이해/구매 결정 쉬움)
- ✅ 예측 가능 (MRR 계산 명확)
- ✅ 팀 확장 = 매출 증가

**단점**:
- ❌ 성장 저항 (팀원 추가 부담)
- ❌ Seat Sharing (1계정 공유)
- ❌ 가치 불일치 (파워 유저 vs 가끔 유저)

**최적화**:
- **Active User 정의**: 월 1회 이상 로그인
- **Viewer/Guest 무료**: Read-only 사용자
- **Volume Discount**: 100명+ 할인

### 2. Usage-Based (사용량 기반)

**공식**: `가격 = 사용량 × 단가`

**예시**:
- Twilio: SMS 1개당 $0.0075
- AWS: 컴퓨팅 시간당 과금
- Stripe: 거래액의 2.9% + $0.30

**장점**:
- ✅ 가치 정렬 (많이 쓸수록 많이 지불)
- ✅ 진입 장벽 낮음 (소량부터 시작)
- ✅ 고객 성장 = 매출 성장

**단점**:
- ❌ 예측 어려움 (월별 변동)
- ❌ Bill Shock (예상 초과 청구)
- ❌ 복잡한 계산

**최적화**:
- **Usage Cap**: 최대 한도 설정
- **Usage Alert**: 80% 도달 알림
- **Commitment Discount**: 최소 사용량 약정 할인

### 3. Flat-Rate (고정 요금)

**공식**: `가격 = 고정액` (사용량 무제한)

**예시**:
- Basecamp: $99/월 (무제한 사용자)
- Netflix: $15.99/월 (무제한 시청)

**장점**:
- ✅ 마찰 없음 (사용 걱정 X)
- ✅ 예측 가능 (고정 비용)
- ✅ 마케팅 단순 ("무제한")

**단점**:
- ❌ 가치 누수 (파워 유저 과소 지불)
- ❌ 업셀 어려움 (이미 무제한)
- ❌ 수익 최적화 한계

**최적 상황**:
- 소규모 SaaS (복잡도 회피)
- 명확한 타겟 (SMB만)
- 브랜드 차별화 ("심플함")

### 4. Tiered (구간별)

**공식**: Good/Better/Best 3-tier

**예시**:
- HubSpot:
  - Starter: $50/월 (1,000 contacts)
  - Professional: $800/월 (10,000 contacts)
  - Enterprise: $3,200/월 (무제한)

**장점**:
- ✅ 업셀 경로 명확
- ✅ 세그먼트별 최적화
- ✅ Price Anchoring 활용

**단점**:
- ❌ 선택 마비 (너무 많으면)
- ❌ 경계 불만 (Tier 경계선 고객)

**최적화**:
- **3-tier 권장** (연구: 3개가 최적)
- **중간 Tier Highlight**: "Most Popular"
- **Enterprise Custom**: 대기업은 별도

### 5. Hybrid (혼합)

**공식**: `Base Fee + Usage 또는 Per-Seat + Feature Tier`

**예시**:
- Salesforce: Base (User) + Add-on (Feature)
- Snowflake: Compute + Storage 분리
- MongoDB Atlas: Cluster Tier + Data Transfer

**장점**:
- ✅ 유연성 (다양한 고객)
- ✅ 수익 최적화
- ✅ Lock-in 강화

**단점**:
- ❌ 복잡도 높음
- ❌ 설명 어려움
- ❌ 청구 시스템 복잡

**최적 상황**:
- Enterprise 고객
- 다양한 Use Case
- 성숙한 제품

---

## 밸류 메트릭 (Value Metric)

### 정의

**밸류 메트릭**: 과금 단위. "무엇을 세어서 과금할 것인가?"

**예시**:
- Slack: Active User
- Mailchimp: Contacts
- Twilio: API Calls
- Stripe: Transaction Volume

### 4가지 평가 기준

| 기준 | 정의 | 예시 (Good) | 예시 (Bad) |
|------|------|-------------|------------|
| **설명 가능성** | 고객이 이해하기 쉬운가? | "사용자 수" | "API Request per 1K batches" |
| **가치 정렬** | 고객 가치와 일치하는가? | "매출 증가" | "데이터베이스 Row" |
| **예측 가능성** | 고객이 비용 예측 가능한가? | "고정 사용자 10명" | "변동 많은 Daily Active" |
| **확장성** | 고객 성장 = 매출 성장? | "거래액" | "로그인 횟수" |

### 설명 가능성 (Understandability)

**나쁜 예**:
- "Compute Unit" (무엇인지 모름)
- "Storage Blocks in 128KB" (복잡)

**좋은 예**:
- "Users" (명확)
- "Projects" (이해 쉬움)
- "Contacts" (직관적)

**테스트**:
- 고객에게 5초 내 설명 가능?
- 엄마도 이해할까?

### 가치 정렬 (Value Alignment)

**나쁜 예**:
- CRM → "Database Rows" (고객은 관심 X)
- 마케팅 툴 → "Email Sent" (스팸 유도)

**좋은 예**:
- CRM → "Revenue Generated" (성과 연결)
- 마케팅 → "Leads Converted" (결과 중심)

**테스트**:
- 고객이 더 쓸수록 더 큰 가치?
- ROI 명확?

### 예측 가능성 (Predictability)

**나쁜 예**:
- "Daily Active Users" (일별 변동 큼)
- "API Calls" (예측 불가)

**좋은 예**:
- "Seats" (고정)
- "Monthly Active Users" (안정적)

**테스트**:
- 다음 달 청구액 예측 가능?
- Surprise Bill 가능성?

### 확장성 (Scalability)

**나쁜 예**:
- "Logins per Month" (한계 있음)
- "Files Uploaded" (포화)

**좋은 예**:
- "Transaction Volume" (무한 성장)
- "Team Size" (회사 성장 = 매출)

**테스트**:
- 고객이 10x 성장 시 우리 매출도 10x?

### 밸류 메트릭 선택 프로세스

**1단계: 후보 나열**
- 가능한 모든 메트릭 브레인스토밍
- 예: Users, Projects, Storage, API Calls, Revenue

**2단계: 4기준 평가**
| 메트릭 | 설명 | 가치 | 예측 | 확장 | 총점 |
|--------|------|------|------|------|------|
| Users | 5 | 3 | 5 | 4 | 17 |
| Projects | 4 | 4 | 4 | 3 | 15 |
| API Calls | 2 | 3 | 2 | 5 | 12 |
| Revenue % | 3 | 5 | 3 | 5 | 16 |

**3단계: Top 2-3 선택**
- 총점 높은 순
- 경쟁사 벤치마크

**4단계: 고객 테스트**
- 10-20명 인터뷰
- "어떤 방식이 공정해 보이나요?"

---

## 가격 심리학 (Pricing Psychology)

### 1. Anchoring (앵커링)

**정의**: 첫 번째 가격이 기준점(Anchor)

**적용**:
- **높은 가격 먼저 표시**: Enterprise → Pro → Starter (좌→우)
- **Original Price 취소선**: ~~$199~~ → $99 (할인 강조)
- **Annual Discount**: $100/월 → $1,000/년 (17% 할인)

**예시**:
```
┌─────────────────────────────────────────┐
│ Enterprise    Pro         Starter       │
│ $499/월      $99/월       $29/월        │
│ (Anchor)     (Target)    (Entry)        │
└─────────────────────────────────────────┘
```

Enterprise가 Anchor → Pro가 "합리적" 느낌

### 2. Decoy Effect (미끼 효과)

**정의**: 의도적으로 덜 매력적인 옵션 추가 → 타겟 선택 유도

**적용**:
- Pro (목표)를 선택하게 하려면
- Decoy: Pro와 비슷한 가격, 기능 적음

**예시**:
```
Starter: $29 (100 contacts)
Pro: $99 (10,000 contacts) ← 목표
Decoy: $79 (1,000 contacts) ← 의도적으로 비효율
```

고객 생각: "Decoy가 $79면 Pro $99가 훨씬 나아"

### 3. Charm Pricing (매력 가격)

**정의**: 끝자리 9 사용 → "저렴" 인식

**적용**:
- $100 → $99
- $1,000 → $997 (또는 $995)

**효과**:
- 연구: $100 대비 $99는 20% 전환율 증가
- 심리적 "한 자리" 낮은 느낌 ($99 = 90번대)

**주의**:
- Enterprise는 X ($999 vs $1,000 차이 미미)
- Premium 브랜드는 정가 ($100)가 품격

### 4. Price Partitioning (가격 분할)

**정의**: 총 가격을 분할 표시 → 저렴 인식

**적용**:
- **월간 표시**: $1,200/년 → $100/월
- **Per User**: $1,000 (10명) → $100/user
- **Base + Add-on**: $50 Base + $10/user

**예시**:
```
Bad:  $1,440/년
Good: $120/월 또는 $12/user/월
```

### 5. Bundling (번들링)

**정의**: 여러 제품/기능 묶어 판매

**전략**:
- **Mixed Bundling**: 개별 + 번들 선택지
  - Feature A: $50
  - Feature B: $30
  - Bundle (A+B): $60 (25% 할인)

**효과**:
- Cross-sell 증가
- 이탈 감소 (더 많은 제품 사용)

---

## Good/Better/Best 패키징

### 3-Tier 구조

```
┌──────────────┬──────────────┬──────────────┐
│   Starter    │     Pro      │  Enterprise  │
│   (Good)     │  (Better)    │    (Best)    │
├──────────────┼──────────────┼──────────────┤
│  Entry       │  Most Popular│   Custom     │
│  $29/월      │  $99/월      │  Contact Us  │
│              │              │              │
│ 기본 기능     │ 고급 기능     │ 모든 기능     │
│ 이메일 지원   │ 우선 지원     │ 전담 매니저   │
│ 1 프로젝트    │ 10 프로젝트   │ 무제한        │
└──────────────┴──────────────┴──────────────┘
```

### Tier별 설계 원칙

#### Starter (Good)

**목적**: 진입 장벽 낮춤, 제품 경험

**특징**:
- 가격: $10-50/월
- 타겟: 개인, 프리랜서, 초소규모
- 기능: 핵심만 (80% Use Case 커버)
- 제한: 사용량 (예: 100 contacts, 1 project)

**제외 기능**:
- Advanced Features (AI, Automation)
- Integration (API, Zapier)
- Support (Self-serve만)

#### Pro (Better)

**목표**: 대부분 고객 (60-70% 선택)

**특징**:
- 가격: $50-200/월
- 타겟: SMB, 팀 (5-20명)
- 기능: 모든 핵심 + 일부 고급
- 제한: 합리적 (10 projects, 10K contacts)

**강조**:
- **"Most Popular" 배지**
- 색상 강조 (파란색 테두리)
- Starter 대비 10x 가치

#### Enterprise (Best)

**목표**: High-value 고객, 업셀 경로

**특징**:
- 가격: $300+ 또는 "Contact Us"
- 타겟: Enterprise (50명+)
- 기능: 모든 것 + 맞춤형
- 제한: 없음 (무제한)

**추가 혜택**:
- Dedicated CSM (고객 성공 매니저)
- SLA (Service Level Agreement)
- Custom Integration
- Onboarding Support

### Tier 간격 (Pricing Ladder)

**권장 배수**: 3-5x

```
Starter: $29
Pro: $99 (3.4x)
Enterprise: $499 (5x)
```

**너무 좁으면** (2x 미만):
- 업그레이드 동기 약함
- 매출 증가 제한

**너무 넓으면** (10x 이상):
- 중간 Tier 누락 (Gap)
- 고객 이탈 위험

---

## Feature Fencing (기능 제한)

### 5가지 Fencing 전략

| 전략 | 설명 | 예시 | 장점 | 단점 |
|------|------|------|------|------|
| **Usage** | 사용량 제한 | 100 vs 10K contacts | 명확, 공정 | 계산 복잡 |
| **Feature** | 기능 on/off | AI 없음 vs 있음 | 차별화 명확 | 개발 부담 |
| **Support** | 지원 수준 | 이메일 vs 전화 | 비용 정렬 | 경험 차이 |
| **SLA** | 응답 시간 | 48h vs 1h | Enterprise 정당화 | 측정 필요 |
| **API** | 통합 제한 | API 없음 vs 무제한 | Lock-in | 개발자 불만 |

### 1. Usage Fencing (사용량)

**예시**:
- Contacts: 100 (Starter) vs 10,000 (Pro)
- Projects: 1 vs 10 vs Unlimited
- Storage: 10GB vs 100GB vs 1TB

**장점**:
- 공정 (많이 쓸수록 많이 지불)
- 이해 쉬움

**주의**:
- Soft Limit (초과 시 업그레이드 유도)
- Hard Limit (차단)은 UX 나쁨

### 2. Feature Fencing (기능)

**예시**:
- AI 기능: Pro 이상
- Automation: Enterprise만
- Custom Branding: Enterprise

**전략**:
- **20% 기능 = 80% 가치**: 핵심 고급 기능만 제한
- **Freemium**: 기본은 무료, 고급만 유료

**주의**:
- 너무 많이 제한 → 불만
- 핵심 가치는 모든 Tier 제공

### 3. Support Fencing (지원)

**예시**:
| Tier | Support |
|------|---------|
| Starter | Self-serve (Help Center) |
| Pro | Email (48h 응답) |
| Enterprise | Phone + Dedicated CSM (1h 응답) |

**장점**:
- 비용 구조 일치 (CSM 비용 높음)
- Enterprise 차별화

### 4. SLA Fencing

**예시**:
| Tier | Uptime SLA | Response Time |
|------|------------|---------------|
| Starter | Best Effort (95%) | N/A |
| Pro | 99.5% | 4h |
| Enterprise | 99.9% | 1h (P1) |

**장점**:
- Enterprise 정당화 (미션 크리티컬)

**주의**:
- 인프라 투자 필요
- 페널티 약정 (SLA 미달 시 환불)

### 5. API/Integration Fencing

**예시**:
- Starter: API 없음
- Pro: 1,000 calls/day
- Enterprise: Unlimited

**장점**:
- Lock-in 강화 (통합 많을수록)

**주의**:
- 개발자 타겟이면 제한 최소화
- API가 핵심 가치면 Free Tier도 제공

---

## 연간 vs 월간 (Annual vs Monthly)

### 비교

| 요소 | Monthly | Annual | Annual 장점 |
|------|---------|--------|-------------|
| **가격** | $100/월 | $1,000/년 ($83/월) | 17% 할인 |
| **현금흐름** | 월별 수금 | 선납 | 즉시 현금 확보 |
| **해지율** | 높음 (월별 리뷰) | 낮음 (연간 약정) | Churn 감소 |
| **세일즈 난이도** | 쉬움 (부담 낮음) | 어려움 (큰 결정) | 고객 심리 장벽 |

### 권장 할인율

**연간 할인**: 15-20%

**계산 예시**:
```
Monthly: $100/월 → $1,200/년
Annual: $1,000/년 ($83/월, 17% 할인)
```

**왜 17%?**
- 10%는 너무 작음 (동기 약함)
- 25%는 너무 큼 (매출 손실)
- 15-20%가 Sweet Spot

### 전략

**1. Annual Default**:
- 기본 표시 Annual → "or $100/월"
- 예: Basecamp, ConvertKit

**2. Monthly Default**:
- 기본 Monthly → "Save 17% with Annual"
- 예: Slack, Zoom

**3. Annual Only** (고급):
- Enterprise는 Annual만
- 이유: 큰 계약, 선납 확보

### 현금흐름 영향

**Monthly**:
```
Year 1: $100 × 12 = $1,200 (분산 수금)
```

**Annual**:
```
Year 1: $1,000 (즉시 전액)
→ 런웨이 연장, 마케팅 투자 가능
```

**Startup 초기**: Annual 강력 추천
- 현금흐름 개선
- Churn 감소
- 예측 가능성

---

## 안티패턴 (Anti-Patterns)

### 1. 너무 많은 Tier

**문제**: 5+ Tier → 선택 마비

**예시**:
- Starter, Basic, Pro, Premium, Enterprise, Ultimate

**해결**:
- **3-Tier 원칙**: Good/Better/Best
- 4개 이상 필요하면 SMB/Enterprise 분리

### 2. 가치 vs 가격 불일치

**문제**: 고객 가치 ≠ 지불 금액

**예시**:
- CRM이 ₩1억 매출 증대 → 가격 ₩10만/월 (과소 과금)
- 단순 알림 앱 → 가격 ₩50만/월 (과다 과금)

**해결**:
- Value-based Pricing
- 고객 ROI 기반 가격 설정

### 3. "Race to the Bottom" (가격 경쟁)

**문제**: 경쟁사 따라 계속 인하 → 마진 소멸

**예시**:
- 경쟁사 $50 → 우리 $45
- 경쟁사 $40 → 우리 $35
- ... 결국 모두 손실

**해결**:
- **차별화된 가치**: 가격 대신 기능/서비스
- **Niche**: 특정 세그먼트 Premium
- **Bundling**: 단독 비교 불가하게

### 4. 잦은 가격 변경

**문제**: 3개월마다 가격 변경 → 고객 혼란, 신뢰 하락

**해결**:
- 연 1-2회만 변경
- 기존 고객 Grandfather (기존 가격 유지 옵션)

### 5. 투명하지 않은 가격

**문제**: "Contact Us"만 → 리드 이탈

**예시**:
- 모든 Tier가 "문의 필요"
- 숨겨진 비용 (Setup Fee, Overage)

**해결**:
- 최소 2개 Tier는 명확한 가격
- Enterprise만 "Contact Us"
- 모든 비용 명시 (No Hidden Fee)

---

## 가격 테스트 및 최적화

### A/B 테스트

**테스트 항목**:
1. **가격 포인트**: $99 vs $129
2. **할인율**: 15% vs 20% Annual
3. **Tier 이름**: Pro vs Business
4. **Anchoring**: Enterprise 먼저 vs 나중
5. **CTA**: "Start Free Trial" vs "Get Started"

**샘플 크기**:
- 최소 100 conversions/variant
- 통계적 유의성 95%+

### Van Westendorp PSM (Price Sensitivity Meter)

**4가지 질문**:
1. "어떤 가격이면 **너무 저렴**해서 품질 의심?"
2. "어떤 가격이면 **저렴**하다고 느낌?"
3. "어떤 가격이면 **비싸**다고 느낌?"
4. "어떤 가격이면 **너무 비싸**서 구매 안 함?"

**분석**:
- 적정 가격 범위: Q2-Q3 교차점
- 최적 가격: Q1-Q4 교차점

### 가격 인상 전략

**언제 인상?**:
- NPS > 40 (고객 만족 높음)
- Churn < 업계 평균
- 신규 기능 출시 (가치 증대)

**얼마나?**:
- 연 10-20%
- 한 번에 크게보다 자주 작게

**기존 고객 처리**:
- **Grandfather**: 기존 가격 유지 (6-12개월)
- **Gradual**: 3개월 유예 후 적용
- **Value 강조**: "신기능 추가로 인한"

---

## 관련 스킬

- **gtm-strategy**: 가격을 GTM 전략에 통합
- **financial-modeling**: 가격 시나리오별 매출 예측
- **startup-metrics**: ARPA, LTV 추적
- **sales-playbook**: 가격 협상 전략

## 팁

- **고객 가치 기준**: 비용 기반이 아닌 고객 ROI 기반 가격
- **3-Tier**: 연구 결과 3개가 최적 (2개는 부족, 4개는 과다)
- **Pro 타겟**: 60-70% 고객이 Pro 선택하도록 설계
- **연간 우선**: 초기 스타트업은 현금흐름 위해 Annual 강력 권장
- **가격 인상 주저 말기**: 가치 있으면 인상. 경쟁사보다 20% 비싸도 OK
- **밸류 메트릭 검증**: 10-20 고객 인터뷰 필수
- **투명성**: 숨겨진 비용 없이 모든 것 명시
- **정기 리뷰**: 분기별 가격 전략 검토, 연 1회 조정
