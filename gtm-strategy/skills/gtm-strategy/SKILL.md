---
name: gtm-strategy
description: Go-to-Market 전략 수립을 안내합니다 — GTM 모션, 콘텐츠 전략, 채널 선택, 브랜드 구축. "GTM", "시장 진입", "고객 획득", "채널 전략", "콘텐츠 마케팅" 등으로 실행합니다.
---

# GTM Strategy

> 익숙하지 않은 플레이스홀더가 보이거나 연결된 도구를 확인하려면 [CONNECTORS.md](../../CONNECTORS.md)를 참조하세요.

Go-to-Market (GTM) 전략 프레임워크입니다. 5가지 GTM 모션, 콘텐츠 피라미드, PESO 채널 분배, 플랫폼별 전략을 조합하여 ICP에 도달하고 효율적으로 성장하는 실행 계획을 수립합니다.

## 작동 방식

```
┌─────────────────────────────────────────────────────────────────┐
│                      GTM STRATEGY FRAMEWORK                      │
├─────────────────────────────────────────────────────────────────┤
│  기본 기능 (단독 작동)                                            │
│  ✓ 제품/ICP 기반 최적 GTM 모션 선정 (5가지 중)                    │
│  ✓ 콘텐츠 피라미드 전략 (Pillar → Derivative → Atomic)          │
│  ✓ PESO 채널 분배 (Paid/Earned/Shared/Owned)                   │
│  ✓ 90일 실행 계획 및 KPI 설정                                     │
├─────────────────────────────────────────────────────────────────┤
│  강화 모드 (도구 연결 시)                                         │
│  + ~~analytics: 채널별 전환율 데이터 수집                         │
│  + ~~knowledge base: 기존 콘텐츠 아카이브 참조                   │
│  + ~~CRM: ICP별 Win Rate 및 채널 기여도 분석                     │
└─────────────────────────────────────────────────────────────────┘
```

## 시작하기

1. **GTM 모션 선택**: "우리 제품에 맞는 GTM 전략은?"
2. **콘텐츠 전략**: "콘텐츠 마케팅 계획을 세워줘"
3. **채널 우선순위**: "어떤 채널에 집중해야 해?"
4. **90일 플랜**: "첫 3개월 GTM 로드맵 만들어줘"

## 5가지 GTM 모션

### 모션 선택 프레임워크

```
          제품 복잡도
               ↑
    Complex    │   Sales-Led    │  Community-Led
               │                │
    ────────────────────────────────────→ ACV
               │                │
    Simple     │   PLG          │  Content-Led
               │                │
          Self-serve ← ─ ─ ─ ─ → High-touch
```

### 1. Product-Led Growth (PLG)

**정의**: 제품 자체가 주요 성장 엔진. 무료 사용 → 가치 경험 → 유료 전환

**최적 상황**:
- Self-serve 가능 (온보딩 < 30분)
- ACV < $10K (신용카드 결제)
- 네트워크 효과 또는 바이럴 요소
- 사용자 = 구매자 (엔드 유저 결정권)

**핵심 지표**:
| 지표 | 목표 | 측정 주기 |
|------|------|-----------|
| **Activation Rate** | >40% | 주간 |
| **PQL (Product Qualified Lead)** | 월 100+ | 월간 |
| **Free → Paid 전환** | 3-10% | 월간 |
| **Time to Value** | <5분 | 코호트 |
| **Viral Coefficient (K)** | >0.5 | 분기 |

**전략**:
1. **Freemium/Free Trial**: 제한 없는 무료 또는 14-30일 Trial
2. **Aha Moment 최적화**: 첫 가치 경험까지 시간 단축
3. **In-product 유도**: Usage 기반 업그레이드 프롬프트
4. **Self-serve Checkout**: 신용카드 결제, 영업 개입 최소

**예시**: Slack, Notion, Figma, Calendly

### 2. Sales-Led

**정의**: 세일즈팀이 주도. 복잡한 솔루션, 높은 ACV, 다수 의사결정자

**최적 상황**:
- ACV > $10K (Enterprise)
- 복잡한 구매 프로세스 (Buying Committee)
- 맞춤형 구현 필요
- Compliance/Security 요구사항

**핵심 지표**:
| 지표 | 목표 | 측정 주기 |
|------|------|-----------|
| **Pipeline Coverage** | 3-5x Quota | 월간 |
| **Win Rate** | 20-40% | 분기 |
| **Sales Cycle** | <90일 (SMB), <180일 (Ent) | 분기 |
| **ACV** | $50K+ | 분기 |
| **Sales Productivity** | >$500K ARR/Rep | 연간 |

**전략**:
1. **Inbound 리드 생성**: 콘텐츠, SEO, Webinar
2. **SDR/BDR 팀**: Lead Qualification 전담
3. **AE (Account Executive)**: 딜 클로징
4. **Solution Engineering**: 기술 데모, POC 지원

**예시**: Salesforce, Workday, ServiceNow

### 3. Community-Led

**정의**: 커뮤니티가 성장 엔진. 사용자가 전도사(Evangelist)

**최적 상황**:
- 개발자/크리에이터 타겟
- 오픈소스 또는 플랫폼
- 강력한 Use Case 다양성
- Bottom-up 채택 (개인 → 팀 → 조직)

**핵심 지표**:
| 지표 | 목표 | 측정 주기 |
|------|------|-----------|
| **Active Community Members** | 월 1,000+ | 월간 |
| **Contribution Rate** | >5% | 월간 |
| **Community → Customer** | 10-20% | 분기 |
| **NPS** | >50 | 분기 |
| **Forum DAU/MAU** | >30% | 주간 |

**전략**:
1. **포럼/Slack/Discord**: 활발한 토론 공간
2. **Contributor Program**: Top 유저 리워드
3. **Events**: 밋업, 컨퍼런스, 해커톤
4. **Content by Community**: 사용자 생성 튜토리얼

**예시**: GitHub, Hashicorp, Stripe (개발자 커뮤니티)

### 4. Content-Led

**정의**: 콘텐츠가 주요 획득 채널. Thought Leadership → Inbound

**최적 상황**:
- 복잡한 문제 (교육 필요)
- 긴 구매 주기 (6-12개월)
- 높은 LTV (장기 고객)
- SEO 기회 풍부

**핵심 지표**:
| 지표 | 목표 | 측정 주기 |
|------|------|-----------|
| **Organic Traffic** | 월 10K+ | 월간 |
| **Content → MQL** | 20-30% | 월간 |
| **Domain Authority** | 50+ (Moz) | 분기 |
| **Backlinks** | 월 50+ | 월간 |
| **Newsletter 구독자** | 분기 20% 성장 | 분기 |

**전략**:
1. **Pillar Content**: 장문 가이드 (5,000+ 단어)
2. **SEO 최적화**: 키워드 리서치, 백링크
3. **멀티 채널 배포**: 블로그 → LinkedIn → 뉴스레터
4. **Lead Magnet**: eBook, 템플릿, 체크리스트

**예시**: HubSpot, Intercom, Drift

### 5. Founder-Led

**정의**: 창업자 개인 브랜드가 성장 엔진. Personal Brand → Company

**최적 상황**:
- 초기 단계 (Pre-seed, Seed)
- 예산 제한 (CAC < $100)
- 창업자가 Thought Leader
- Niche 시장

**핵심 지표**:
| 지표 | 목표 | 측정 주기 |
|------|------|-----------|
| **Founder Followers** | 분기 20% 성장 | 분기 |
| **Post Engagement** | >5% | 주간 |
| **Inbound DM/이메일** | 주 10+ | 주간 |
| **Speaking/Podcast** | 월 2+ | 월간 |
| **Newsletter → Customer** | 5-10% | 분기 |

**전략**:
1. **LinkedIn/X 일일 포스팅**: 인사이트, 경험 공유
2. **Founder 뉴스레터**: 주간/격주 발행
3. **Podcast 게스트**: 타겟 청중 있는 쇼
4. **Speaking**: 컨퍼런스, 웨비나

**예시**: Sahil Lavingia (Gumroad), Pieter Levels (Nomad List)

### 모션 조합 (Hybrid)

대부분 스타트업은 **2-3개 모션 조합**:

**예시 조합**:
- **PLG + Community**: Notion (무료 사용 + 활발한 템플릿 커뮤니티)
- **Content + Sales**: HubSpot (블로그로 리드 → 세일즈 전환)
- **Founder + PLG**: Linear (CEO 트위터 + 제품 바이럴)
- **Community + Sales**: Slack (팀 내 확산 + Enterprise 세일즈)

**선택 기준**:
1. **Primary Motion**: 70% 리소스 (주 엔진)
2. **Secondary Motion**: 20% 리소스 (보완)
3. **Experimental**: 10% 리소스 (테스트)

---

## 콘텐츠 피라미드

### 3-Tier 구조

```
         🔺 Pillar Content (월 1-2개)
        /  \   - 5,000+ 단어 가이드
       /    \  - 포괄적, SEO 최적화
      /      \ - 재사용 가능 자산
     ──────────
    /          \
   / Derivative \  (주 3-5개)
  /   Content    \ - 블로그 포스트
 /                \ - 비디오, 팟캐스트
──────────────────
       Atomic        (일 1-3개)
      Content        - 소셜 미디어 포스트
    (Bite-sized)     - 인포그래픽
                     - Short-form 비디오
```

### Pillar Content (기둥 콘텐츠)

**정의**: 포괄적, 권위적 리소스. 1년 이상 evergreen

**유형**:
1. **Ultimate Guide**: "The Complete Guide to [Topic]"
2. **Industry Report**: 자체 조사 데이터
3. **Framework/Methodology**: 독자적 프레임워크
4. **Resource Hub**: 도구, 템플릿 모음

**예시**:
- HubSpot "The Ultimate Guide to Email Marketing"
- Moz "Beginner's Guide to SEO"
- First Round Review "State of Startups Report"

**제작 주기**: 월 1-2개 (고품질 우선)

### Derivative Content (파생 콘텐츠)

**정의**: Pillar에서 파생된 콘텐츠. 특정 주제 심화

**유형**:
1. **블로그 포스트**: Pillar의 한 챕터 확장
2. **비디오**: 핵심 개념 설명
3. **Podcast 에피소드**: 전문가 인터뷰
4. **Webinar**: 실습형 워크샵

**예시**:
- Pillar: "Complete Guide to CRM"
  - Derivative 1: "10 CRM Mistakes to Avoid"
  - Derivative 2: "How to Migrate from Excel to CRM" (Video)
  - Derivative 3: "CRM ROI Calculator" (Tool)

**제작 주기**: 주 3-5개

### Atomic Content (원자 콘텐츠)

**정의**: 소셜 미디어용 bite-sized. 즉시 소비 가능

**유형**:
1. **LinkedIn 포스트**: 인사이트, 스토리
2. **X (Twitter) 스레드**: Tip, 프레임워크
3. **Short-form 비디오**: TikTok, Reels, Shorts
4. **인포그래픽**: 통계, 프로세스

**예시**:
- Pillar 통계 → 인포그래픽
- Derivative 인용 → LinkedIn 캐러셀
- 비디오 클립 → Reels

**제작 주기**: 일 1-3개

### 콘텐츠 재활용 (Repurposing)

**1개 Pillar → 50+ Atomic**:
```
Ultimate Guide (Pillar)
  ↓
├─ 10 Blog Posts (Derivative)
├─ 5 Videos (Derivative)
├─ 1 Podcast Series (5 eps)
│
└─ 각 Derivative에서:
   ├─ 5 LinkedIn Posts
   ├─ 10 Tweets
   ├─ 3 Infographics
   └─ 5 Short Videos

총: 1 Pillar → 20 Derivative → 50+ Atomic
```

---

## PESO 채널 분배 모델

### 4-Channel 프레임워크

| 채널 | 정의 | 통제 수준 | 비용 | 속도 | 신뢰도 |
|------|------|-----------|------|------|--------|
| **Paid** | 광고 구매 | 高 | 高 | 빠름 | 中 |
| **Earned** | PR, 언론 | 低 | 低 | 느림 | 高 |
| **Shared** | 소셜 미디어 | 中 | 中 | 중간 | 中 |
| **Owned** | 자사 채널 | 高 | 中 | 중간 | 高 |

### Paid (유료)

**채널**:
- Google Ads (Search, Display)
- LinkedIn Ads (B2B)
- Facebook/Instagram Ads (B2C)
- Sponsored Content (뉴스레터, 팟캐스트)

**전략**:
- **Bottom Funnel 우선**: 구매 의도 높은 키워드
- **Retargeting**: 웹사이트 방문자 재타겟
- **Lookalike**: 기존 고객 유사 오디언스
- **ROI 추적**: CAC < LTV/3

**예산 배분**:
- Seed: 10-20% (실험 단계)
- Series A: 30-40% (확장)
- Series B+: 40-50% (규모화)

### Earned (획득)

**채널**:
- 언론 보도 (TechCrunch, 매경 등)
- 게스트 블로깅
- 팟캐스트 게스트
- 인플루언서 멘션

**전략**:
- **Newsjacking**: 트렌드 이슈에 빠르게 반응
- **Data Story**: 독점 데이터로 PR
- **Founder Story**: 창업 배경, 도전 과제
- **미디어 킷**: Press Kit, 고해상도 로고, 팩트 시트

**측정**:
- Domain Authority 향상
- Backlink 수
- Brand Search Volume 증가

### Shared (공유)

**채널**:
- LinkedIn (B2B)
- X/Twitter (Tech, Thought Leadership)
- YouTube (튜토리얼)
- Reddit, Hacker News (개발자)

**전략**:
- **일관성**: 주 3-5회 포스팅
- **Engagement**: 댓글 응답, 대화 참여
- **Employee Advocacy**: 팀원 계정 활용
- **Hashtag**: 브랜드 + 산업 태그

**측정**:
- Engagement Rate (>3%)
- Follower Growth (월 10%)
- Social → Website 트래픽

### Owned (소유)

**채널**:
- 블로그
- 이메일 뉴스레터
- Podcast
- YouTube 채널
- 커뮤니티 (Slack, Discord)

**전략**:
- **SEO**: 검색 의도 맞춤 콘텐츠
- **Email List**: Lead Magnet으로 구독 유도
- **Personalization**: 세그먼트별 맞춤 콘텐츠
- **Evergreen**: 시간 지나도 유효한 자산

**측정**:
- Organic Traffic (월 20% 성장)
- Email Open Rate (>20%)
- Newsletter → MQL (10-20%)

### PESO 배분 전략

**단계별 권장 배분**:

| 단계 | Paid | Earned | Shared | Owned |
|------|------|--------|--------|-------|
| **Pre-seed** | 10% | 20% | 30% | 40% |
| **Seed** | 20% | 20% | 30% | 30% |
| **Series A** | 35% | 15% | 25% | 25% |
| **Series B+** | 45% | 10% | 20% | 25% |

**초기 (Pre-seed/Seed)**: Owned 중심 (낮은 CAC, 장기 자산)
**성장 (Series A+)**: Paid 확대 (빠른 확장, 예측 가능)

---

## 플랫폼별 전략

### LinkedIn (B2B)

**최적 ICP**: 의사결정자, 직장인

**콘텐츠 유형**:
1. **Personal Insight**: 경험, 실패담
2. **Industry Trend**: 시장 분석, 예측
3. **How-to**: 실용적 팁
4. **Behind-the-Scenes**: 팀, 문화

**포스팅 빈도**: 주 3-5회

**포맷**:
- 텍스트: 1,300자 (3-paragraph sweet spot)
- 캐러셀: 10-slide 프레임워크
- 비디오: 1-3분 (네이티브 업로드)

**성장 전략**:
- 댓글 참여 (포스팅 후 1시간)
- Engagement Pod (피어 그룹)
- 해시태그 3-5개

**측정**: Impression, Engagement Rate, Profile View → Connection

### X (Twitter)

**최적 ICP**: Tech, 스타트업, 개발자

**콘텐츠 유형**:
1. **스레드**: 프레임워크, 스토리
2. **Quick Tip**: 한 줄 인사이트
3. **Meme/Humor**: 공감 유발
4. **Poll**: 커뮤니티 참여

**포스팅 빈도**: 일 1-5회

**포맷**:
- 280자 이내 (간결)
- 이미지/GIF (참여 2x)
- 스레드 (긴 내용)

**성장 전략**:
- Reply Guy (업계 리더 댓글)
- Retweet with Comment
- Quote Tweet (의견 추가)

**측정**: Follower 성장, Engagement Rate, Link Click

### 뉴스레터

**최적 ICP**: 깊은 관계, 장기 고객

**콘텐츠 유형**:
1. **Weekly Digest**: 주간 인사이트
2. **Expert Interview**: 게스트 Q&A
3. **Case Study**: 고객 성공 사례
4. **Product Update**: 신기능 소개

**발행 빈도**: 주간 또는 격주

**포맷**:
- Subject Line: 40자 이내, 호기심
- Preview Text: 100자 요약
- Body: 스캔 가능 (헤더, 불릿)
- CTA: 1개 명확한 액션

**성장 전략**:
- Lead Magnet (eBook, 템플릿)
- 블로그 하단 CTA
- LinkedIn/X 프로모션

**측정**: Open Rate (>20%), Click Rate (>3%), Unsubscribe (<0.5%)

### Podcast

**최적 ICP**: 출퇴근, 운동 중 청취

**콘텐츠 유형**:
1. **Founder Interview**: 창업 스토리
2. **Industry Expert**: 전문가 인사이트
3. **Solo Episode**: 프레임워크 설명
4. **Debate/Panel**: 다양한 관점

**에피소드 길이**: 30-45분 (통근 시간)

**포맷**:
- Intro: 30초 (오늘 내용 요약)
- Main: 25-40분 (인터뷰/토론)
- Outro: 2분 (CTA, 후원사)

**배포**:
- Apple Podcasts, Spotify
- YouTube (비디오 버전)
- 블로그 (트랜스크립트)

**측정**: Downloads, Listener Retention, CTA Click

---

## 브랜드 아키텍처

### 회사 vs 개인 브랜드

| 요소 | 회사 브랜드 우선 | 개인 브랜드 우선 |
|------|------------------|------------------|
| **초점** | 제품, 솔루션 | 창업자, 철학 |
| **장점** | 확장 용이, 팀 강조 | 신뢰 빠름, 진정성 |
| **단점** | 초기 신뢰 구축 느림 | 창업자 의존도 높음 |
| **예시** | Salesforce, Adobe | Tesla (Elon), Basecamp (DHH) |

**권장 조합** (초기 스타트업):
- **Seed 이전**: 개인 70% + 회사 30%
  - 창업자 브랜드로 초기 트랙션
  - 회사 계정 병행 (장기 자산)
- **Series A+**: 회사 60% + 개인 40%
  - 팀 확장, 제품 중심으로 전환
  - 창업자는 Thought Leader 유지

### Founder-Led Marketing

**전략**:
1. **창업자 = Chief Storyteller**
   - 회사 비전, 미션 전도
   - 제품 결정 배경 공유

2. **Authentic Voice**
   - 실패, 도전 과제 솔직히
   - "우리는 완벽하지 않다" 인정

3. **Consistent Cadence**
   - 주 3-5 포스트 (LinkedIn/X)
   - 주간 뉴스레터
   - 월 1-2 팟캐스트

**주의사항**:
- 개인 vs 회사 경계 명확
- 팀 크레딧 (창업자만 부각 X)
- 은퇴/퇴사 시 리스크 고려

---

## 안티패턴 (Anti-Patterns)

### 1. 플랫폼 FOMO

**증상**: 모든 채널 동시 실행 → 분산, 효과 없음

**예시**:
- LinkedIn, X, Instagram, TikTok, YouTube 동시 시작
- 각 채널 주 1회 미만 포스팅
- 일관성 없음

**해결**:
- **1-2 플랫폼 집중** (ICP가 있는 곳)
- 3개월 실험 → 데이터 기반 결정
- 나머지는 Repurpose만

### 2. 배포 없는 콘텐츠

**증상**: 고품질 콘텐츠 제작 → 블로그 발행 → 배포 안 함

**예시**:
- 블로그 포스트 발행 후 종료
- 소셜 미디어 공유 1회
- 이메일 발송 없음

**해결**:
- **제작 30% + 배포 70%**
- 1개 콘텐츠 → 10개 채널 배포
- 첫 48시간 집중 푸시

### 3. 경쟁사 모방

**증상**: 경쟁사 전략 그대로 복사 → 차별화 없음

**예시**:
- "A사가 LinkedIn 하니까 우리도"
- 메시지, 톤도 유사
- 독자적 POV 없음

**해결**:
- **차별화된 관점** (Unique POV)
- 경쟁사 반대 입장 (Contrarian)
- 자사 데이터, 경험 기반

### 4. Vanity Metrics 집착

**증상**: 팔로워 수, Impression만 추적 → 비즈니스 영향 무시

**예시**:
- 팔로워 10K 목표
- 실제 MQL, 고객 전환 0

**해결**:
- **North Star**: MQL, Customer
- 중간 지표: CTR, Email 가입
- Vanity는 보조

### 5. 일관성 부족

**증상**: 2주 집중 → 1개월 중단 → 반복

**예시**:
- "이번 분기는 콘텐츠 집중"
- 한 달 후 중단
- 다음 분기 다시 시작

**해결**:
- **지속 가능한 케이던스**
  - 주 1회라도 꾸준히
  - 팀원 로테이션
  - 콘텐츠 캘린더 (3개월 사전 계획)

---

## 90일 GTM 실행 계획

### Week 1-4: Foundation

**목표**: GTM 모션 확정, ICP 정의, 채널 선택

**액션**:
- [ ] ICP 워크샵 (3-5 페르소나)
- [ ] GTM 모션 선정 (Primary + Secondary)
- [ ] 경쟁사 채널 분석
- [ ] PESO 배분 전략 수립
- [ ] 콘텐츠 캘린더 (12주)
- [ ] Baseline 측정 (현재 트래픽, 팔로워)

**Deliverable**:
- GTM Strategy Doc (10페이지)
- Content Calendar (Q1)

### Week 5-8: Launch

**목표**: 채널 오픈, 초기 콘텐츠 발행, 피드백 수집

**액션**:
- [ ] Pillar Content 1개 발행
- [ ] Derivative 10개 배포
- [ ] Owned 채널 셋업 (블로그, 뉴스레터)
- [ ] Shared 계정 활성화 (LinkedIn, X)
- [ ] Paid 실험 ($1K 예산)
- [ ] A/B 테스트 (헤드라인, CTA)

**Deliverable**:
- 1 Pillar + 10 Derivative
- 300+ Email 구독자
- 100+ Organic Traffic/day

### Week 9-12: Optimize

**목표**: 데이터 분석, 최적화, 확장 준비

**액션**:
- [ ] 채널별 ROI 분석
- [ ] Top 3 콘텐츠 Repurpose
- [ ] Paid 확대 (효과 좋은 채널)
- [ ] 파트너십 (게스트 블로깅)
- [ ] Customer Interview (Win 사례)
- [ ] Q2 전략 조정

**Deliverable**:
- GTM Performance Report
- Q2 Roadmap (우선순위 조정)

---

## 관련 스킬

- **pricing-strategy**: GTM과 가격 전략 연계
- **sales-playbook**: Sales-Led 모션 실행
- **competitive-landscape**: 경쟁사 GTM 분석
- **startup-metrics**: 채널별 전환율 추적

## 팁

- **Focus**: 2-3 채널 집중이 10개 분산보다 효과적
- **Consistency > Quality**: 완벽한 콘텐츠 월 1개보다 괜찮은 콘텐츠 주 1개
- **Repurpose**: 1개 콘텐츠를 10가지 형식으로 재활용
- **Data-Driven**: 60일 실험 → 데이터 기반 결정
- **Founder Voice**: 초기 단계는 창업자 브랜드가 강력
- **Long Game**: 콘텐츠 마케팅은 6-12개월 후 효과
- **Community First**: 판매 전에 관계, 신뢰 구축
- **Authenticity**: 과장보다 솔직함이 장기적으로 유리
