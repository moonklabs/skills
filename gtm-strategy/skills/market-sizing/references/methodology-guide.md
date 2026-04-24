# Market Sizing Methodology Guide

Detailed step-by-step execution guide for 3 methodologies (Top-down, Bottom-up, Value Theory) with real-world examples.

## Table of Contents

1. [Top-down Methodology](#top-down-methodology)
2. [Bottom-up Methodology](#bottom-up-methodology)
3. [Value Theory Methodology](#value-theory-methodology)
4. [Cross-Validation (Triangulation)](#cross-validation-triangulation)
5. [Industry Best Practices](#industry-best-practices)

---

## Top-down Methodology

### Overview

**Definition**: Start with entire market size, progressively narrow via filters to reach target market

**Best For**:
- Mature industries (abundant reports)
- Initial estimation (quick Sanity Check)
- Global expansion planning (multi-region comparison)

**Advantages**:
- Fast execution (1-2 hours)
- Leverage existing industry reports
- Understand big picture

**Disadvantages**:
- Many assumptions = large error margin
- Over-estimate tendency
- Weak connection to execution plan

### 8-Step Process

#### Step 1: Define Broadest Category

**Question**: "What's the widest category our product fits?"

**Examples**:
- CRM SaaS → "Enterprise Software"
- Used car marketplace → "Automotive Distribution"
- Fitness app → "Healthcare & Wellness"

**Data Sources**:
- Gartner, IDC, Forrester (paid, high accuracy)
- Statista, Grand View Research (partial free)
- Public company IR (market background sections)

#### Step 2: Find Global Market Size

**Search Queries**:
```
"global [category] market size 2024"
"[category] market forecast 2024-2029"
"total addressable market [category]"
```

**Important**:
- Check multiple sources (±20% variance normal)
- Verify publication date (2-3 years old? adjust with CAGR)
- Confirm "CRM" scope varies by report

**Example**:
```
Source: Gartner "CRM Software Market, Worldwide, 2024"
Global CRM: $69B (2024) → $96B (2028, 8.5% CAGR)
```

#### Step 3: Apply Regional Filter

**Korea Market Typical Ratio**:
- SaaS/Software: 1.5-2.5% of global
- E-commerce/Marketplace: 2-3%
- Consumer apps: 1-2% (population-based)
- Manufacturing/Hardware: 3-5%

**Data Sources**:
- Domestic: KAIT, KISA, Statistics Korea, industry associations
- Comparison: World Bank, UN, OECD country data

**Calculation Example**:
```
Global CRM $69B
Korea is 10th largest economy, 2% IT spend
→ Korea CRM = $69B × 2% = $1.38B

Validation:
Korea IT services $50B (KAIT)
CRM is 2-3% of IT services
→ $1-1.5B (consistent ✓)
```

#### Step 4: Segment Filter (Customer Type)

**B2B Segments**:
- Company size: SMB (<100) / Mid-Market (100-1K) / Enterprise (>1K)
- Industry: Manufacturing, Finance, Retail, Healthcare
- Revenue: <₩100B / ₩100-500B / >₩500B

**B2C Segments**:
- Age: Teens, 20-30, 40-50, 60+
- Geography: Metro / Major cities / Regional
- Income: Top 20% / Middle class / Bottom

**Example** (CRM for SMB):
```
Korea CRM $1.38B
SMB (10-500 employees) share: 65%
→ SMB CRM = $1.38B × 65% = $897M
```

**Data Sources**:
- SME Office "SMB Status"
- Statistics Korea business statistics
- Industry association reports

#### Step 5: Product/Channel Filter

**SaaS Examples**:
- On-premise vs Cloud (cloud adoption rate)
- Vertical SaaS vs Horizontal
- SMB Self-serve vs Enterprise Sales

**Marketplace Examples**:
- Offline vs Online (online penetration)
- C2C vs B2C vs B2B
- Region-based vs National

**Consumer Examples**:
- Mobile vs Web
- Subscription vs Ad-based
- Social vs Utility

**Example** (Cloud CRM):
```
SMB CRM $897M
Cloud-based: 45% (rest is on-premise/Excel)
→ Cloud CRM SAM = $897M × 45% = $403M
```

#### Step 6: Apply Adoption/Conversion Rate

**Question**: "Of target segment, what % will actually use our solution?"

**Considerations**:
- Current solution satisfaction
- Switching cost (time, money, risk)
- Budget availability
- Category maturity

**Typical Ranges**:
- New category: 5-15% (education needed)
- Replace existing: 30-60% (pain point clear)
- Mandatory (compliance): 70-90%

**Example**:
```
Cloud CRM SAM $403M
Cloud adoption intent: 50%
→ Adjusted SAM = $403M × 50% = $201.5M ≈ $200M
```

#### Step 7: Confirm SAM

**SAM (Serviceable Available Market)**:
- "Market we can reach with our business model"
- Final value after all filters

**Sanity Check**:
- SAM = 10-50% of TAM (typical)
- <10%: Segment too narrow?
- >50%: Filters insufficient?

#### Step 8: Calculate SOM (Market Share Goal)

**SOM (Serviceable Obtainable Market)**:
- "Realistic capture in 3-5 years"

**Market Share Goals**:

| Market Situation | 3-Year | 5-Year | Rationale |
|------------------|--------|--------|-----------|
| **New Category** | 5-10% | 10-20% | First-mover advantage |
| **Fragmented Market** | 3-7% | 7-15% | Many competitors, share diluted |
| **Oligopoly** | 1-3% | 3-5% | Incumbents strong |

**Example**:
```
SAM $200M (fragmented market, top 3 = 15% each)
5-year goal: 5% market share
→ SOM = $200M × 5% = $10M

Reverse-check:
$10M ÷ $50K ACV = 200 customers
Korea SMB 20K total ÷ 200 = 1%
→ Realistic ✓
```

### Top-down Checklist

- [ ] Global market size (2+ sources)
- [ ] Regional ratio (Korea 1.5-3%)
- [ ] Segment filters (clear criteria)
- [ ] Channel/Product filters (cloud, mobile, etc.)
- [ ] Adoption rate (realistic, not optimistic)
- [ ] SAM in 10-50% of TAM range
- [ ] SOM reverse-validated (customer count needed)
- [ ] Data sources + publication years documented

---

## Bottom-up Methodology

### Overview

**Definition**: Start from unit economics (per-customer revenue), aggregate to market size

**Best For**:
- Validated Unit Economics exist (beta customers)
- Clear ICP (Ideal Customer Profile)
- Planning execution (SOM → needed customers)

**Advantages**:
- Most accurate (real data-based)
- Directly connects to execution
- High investor confidence

**Disadvantages**:
- Time-intensive (data collection)
- Early stage: ARPA uncertain
- May under-estimate market growth potential

### 7-Step Process

#### Step 1: Define ICP (Ideal Customer Profile)

**B2B Example**:
```
Industry: Manufacturing
Employee Count: 50-200
Revenue Size: ₩100-500B
Geography: Korea (Seoul priority)
IT Maturity: ERP already in use
Main Pain: Inventory inefficiency
```

**B2C Example**:
```
Age: 25-40
Occupation: Full-time employed (40+ hrs/week)
Location: Metro area
Interests: Fitness, health
Pain Point: Limited time, can't use PT
```

#### Step 2: Count Total Target Customers

**B2B Sources**:
- Statistics Korea "National Business Survey"
- SME Office "SMB Status"
- Industry associations (e.g., Korea Manufacturing Assoc.)
- Public data portal

**B2C Sources**:
- Statistics Korea "Population Census"
- Government "Resident Population Statistics"
- Agency data (Ministry of Culture, Health Ministry)

**Calculation Example** (Manufacturing ERP):
```
Korea manufacturers: 87,000 (Statistics Korea)
Size 50-200 employees: 8% = 6,960
Revenue ₩100-500B: 70% of above = 4,872
Without ERP currently: 30% = 1,462
→ Target audience: ~1,500
```

#### Step 3: Set ARPA/ACV

**ARPA** = Average Revenue Per Account

**Data Hierarchy**:
1. **Your beta customer data** (best)
2. **Competitor disclosures** (public filings, SaaS benchmarks)
3. **Pricing page pricing** (make assumptions about mix)
4. **Customer interviews** (willingness-to-pay surveys)

**Setting Method 1: Price Sheet-Based**:
```
Starter: ₩100K/month (expect 30%)
Pro: ₩300K/month (expect 50%)
Enterprise: ₩1M/month (expect 20%)

Blended ARPA = ₩100K×30% + ₩300K×50% + ₩1M×20%
             = ₩30K + ₩150K + ₩200K
             = ₩380K/month
```

**Setting Method 2: Competitor Reverse-Engineering**:
```
Competitor A: $50M ARR, 1,000 customers → $50K ACV
Competitor B: $30M ARR, 800 customers → $37.5K ACV
Our target: $40K ACV (midpoint)
```

**Setting Method 3: Customer Research**:
```
Survey 20 customers:
- ₩200K/month: 25%
- ₩300K/month: 50%
- ₩500K/month: 25%

Median: ₩300K/month
```

#### Step 4: Calculate TAM (Theoretical Max)

**Formula**:
```
TAM = Total Target Customers × ARPA × 12 (annualize)
```

**Example** (Manufacturing ERP):
```
Customers: 1,500
ARPA: ₩500K/month
TAM = 1,500 × ₩500K × 12 = ₩900B (~$7.5M)
```

**Sanity Check**:
- Compare to Top-down result (±30% OK)
- Too small: ICP too narrow?
- Too large: Customer count over-estimated?

#### Step 5: Apply Reach Filter (SAM)

**Question**: "Of total targets, realistically how many can we reach?"

**By Channel**:

| Channel | Reach | Why |
|---------|-------|-----|
| **Direct Sales** | 20-40% | Sales team capacity limit |
| **Inbound (SEO/Content)** | 10-30% | Search volume, brand awareness |
| **Partner Channel** | 30-60% | Partner network scope |
| **PLG (Self-serve)** | 50-80% | Internet accessible |

**Example** (Direct Sales Model):
```
TAM: 1,500 customers
Sales team: 5 people
Coverage per person: 100 accounts = 500 total (33%)
SAM = 1,500 × 33% = 500 customers = $2.5M
```

#### Step 6: Apply Conversion Rate (SOM)

**Sales Funnel Conversion** (B2B SaaS typical):
```
Leads (100%)
  ↓ 10-20% (MQL threshold)
Marketing Qualified (10-20%)
  ↓ 30-50% (SQL = demo done)
Sales Opportunity (3-10%)
  ↓ 20-40% (Win rate)
Customer (1-4%)
```

**Example**:
```
SAM: 500 prospects
Lead → Opportunity: 15%
Opportunity → Customer: 25%
Overall: 15% × 25% = 3.75%

Customers = 500 × 3.75% = 18.75 ≈ 20
SOM = 20 × ₩600K (annual ACV) = ₩1.2B
```

**By Maturity**:
- Pre-seed: 1-2% (manual sales)
- Seed: 2-4% (validated playbook)
- Series A+: 5-10% (automated funnel)

#### Step 7: Add Time Dimension (3-5 Year Growth)

**Growth Drivers**:
1. **Customer count**: More sales reps, better marketing
2. **ARPA increase**: Upsell, cross-sell, price increases
3. **Reach increase**: Brand awareness, partnerships

**Example** (5-Year Plan):
```
Year 1: 20 customers × ₩600K = ₩1.2B
Year 2: 50 customers × ₩650K = ₩3.25B (ARPA +8%)
Year 3: 100 customers × ₩700K = ₩7B
Year 4: 180 customers × ₩750K = ₩13.5B
Year 5: 300 customers × ₩800K = ₩24B

5-year SOM: ₩24B (~$2M ARR)
```

### Bottom-up Checklist

- [ ] ICP clearly defined (3-5 criteria)
- [ ] Target customer count (credible source)
- [ ] ARPA/ACV (actual data or benchmarked)
- [ ] Reach percentage (channel-realistic)
- [ ] Conversion rate (funnel historical)
- [ ] Year-by-year growth (drivers explicit)
- [ ] Reverse-validate SOM (needed customers realistic?)

---

## Value Theory Methodology

### Overview

**Definition**: Based on economic value customer receives (savings or revenue gain)

**Best For**:
- New categories (no market data)
- 10x innovation products
- Clear B2B ROI (cost savings)

**Advantages**:
- Fits new markets
- Emphasizes differentiation
- Grounds pricing in value

**Disadvantages**:
- Subjective (hard to prove)
- Behavior change gap (value recognized ≠ adoption)
- Investor skepticism possible

### 5-Step Process

#### Step 1: Calculate Current Solution Cost

**Cost Components** (HR Recruitment):
```
Direct:
- Recruiter fee: 20-30% of annual salary
- Job board subscription: ₩50K/month
- Ad spend: ₩100K/month

Indirect:
- HR time: 40h/month × ₩50K/hour = ₩2M
- Interview time: 20h/month × ₩100K/hour = ₩2M
- Bad hires: 1/year × ₩50M loss = ₩50M/year

Total: ₩80M/year (SMB average)
```

**B2C Example** (Taxi vs Rideshare):
```
Current (Taxi):
- Monthly: 20 trips × ₩15K = ₩300K

Alternative (Own car):
- Fuel + insurance + depreciation: ₩500K/month

Our Service (Carpool):
- 20 trips × ₩8K = ₩160K
→ ₩140K monthly savings vs taxi
```

#### Step 2: Calculate Our Value

**Value Types**:

1. **Cost Savings** (Reduction):
   - Labor cost decrease
   - Tool consolidation (replace 5 → 1)
   - Efficiency gains (time saved)

2. **Revenue Uplift** (Addition):
   - Conversion rate improvement
   - Average order value increase
   - New channel enablement

3. **Risk Mitigation** (Prevention):
   - Compliance violation avoidance
   - Security incident prevention
   - Reputation damage avoidance

**Example** (AI Recruiting):
```
Current cost: ₩80M/year

Savings:
- Recruiter fee 80% cut: -₩40M
- HR time 50% saved: -₩12M
- Bad hires 30% reduction: -₩15M
Total: ₩67M savings

Our price: ₩12M/year
Net benefit: ₩55M/year
ROI: 458%
```

#### Step 3: Estimate Willingness to Pay

**General Rule**: Customers pay 10-30% of created value

**By Type**:
- B2B SaaS: 20-30% (clear ROI)
- Marketplace: 10-20% (transaction fees)
- Consumer: 10-20% (price sensitive)

**Example**:
```
Value created: ₩67M/year
Willingness to pay (30%): ₩20.1M
Our price: ₩12M (60% of willingness)
→ Attractive to customer ✓

Price anchoring:
"Recruiter would cost ₩40M vs us ₩12M"
→ "Save ₩28M, pay ₩12M, net ₩16M"
```

#### Step 4: Calculate TAM

**Formula**:
```
TAM = Total Target Customers × Our Annual Price
```

**Example**:
```
Korea SMB (50-200 employees): 5,000
Our price: ₩12M/year
TAM = 5,000 × ₩12M = ₩600B (~$50M)
```

#### Step 5: Set Adoption Target (SOM)

**Adoption Barriers** (4 Levels):
1. **Awareness**: Know we exist?
2. **Trust**: Believe our value claim?
3. **Switching Cost**: Easy to change?
4. **Urgency**: Must fix now?

**Adoption Targets** (5-year):
- New category: 3-7% (education needed)
- Existing solution replacement: 10-20% (pain clear)
- Mandatory: 30-50% (required)

**Example**:
```
TAM: ₩600B (5,000 customers)
Category: Replacing recruiters (adoption 10%)
SOM = ₩600B × 10% = ₩60B (500 customers)
```

### Value Theory Checklist

- [ ] Current solution cost (direct + indirect)
- [ ] Our value creation (savings or uplift quantified)
- [ ] Beta customer validation (actual ROI data)
- [ ] Willingness to pay (value × 10-30%)
- [ ] Adoption barriers (4-factor analysis)
- [ ] Realistic adoption rate (time-based)

---

## Cross-Validation (Triangulation)

### Why All 3 Methods?

**Each has blind spots**:
- Top-down: Over-optimistic
- Bottom-up: Over-conservative
- Value Theory: Subjective

→ 3 results in agreement = **high confidence**

### Validation Process

#### 1. Run Independently

Do not let one methodology influence another

#### 2. Compare in Table

```
| Method | TAM | SAM | SOM (5y) | Notes |
|--------|-----|-----|---------|-------|
| Top-down | $200M | $50M | $5M | Gartner-based |
| Bottom-up | $180M | $45M | $3M | 1,500 × $50K ACV |
| Value Theory | $250M | $60M | $6M | ₩67M savings |
| **Average** | **$210M** | **$52M** | **$4.7M** | |
| **Std Dev** | ±$29M (14%) | ±$6M (12%) | ±$1.2M (26%) | |
```

#### 3. Assess Consistency

- **±20% or less**: Confident → use average
- **±20-50%**: Medium → review assumptions
- **±50%+**: Low → re-run, find discrepancy

**Above Example**: TAM ±14%, SAM ±12%, SOM ±26%
- TAM & SAM: Good consistency
- SOM: Wider range (conversion assumptions differ)

#### 4. Investigate Differences

**Why is Bottom-up ($3M) lower than Value Theory ($6M)?**:
- Bottom-up: Conservative 3.75% conversion
- Value Theory: 10% adoption (may be optimistic)

**Resolution**: 
- Adjust Bottom-up to 5% conversion → $5M
- Now range is ±20% (better)

#### 5. Choose Final Value

**Investor Presentation**:
- Use mid-range or lower 25%
- Conservative builds credibility
- Say "conservative estimate"

**Internal Planning**:
- Use upper range as stretch goal
- Actual target = medium

**Example**:
```
Investor pitch: "Conservative SOM: $3-5M"
Internal goal: "Target $5M, stretch $6M"
```

---

## Industry Best Practices

### SaaS

**Recommended Methodology Order**:
1. Bottom-up (if ARPA data exists)
2. Top-down (for validation)
3. Value Theory (if ROI clear)

**Key Adjustments**:
- ARPA by tier mix (not blended average)
- Account for churn/expansion
- Net Revenue Retention matters

**Example**:
```
ICP: 50-200 employee manufacturers
Korea targets: 4,000
ARPA: ₩500K/month
Reach: 30% (sales-based)
Convert: 5%
→ SOM = 4,000 × 30% × 5% × ₩6M = ₩36B
```

### Marketplace

**Recommended Methodology Order**:
1. Bottom-up (GMV × Take Rate)
2. Top-down (offline market conversion)
3. Value Theory (transaction cost savings)

**Key Adjustments**:
- GMV vs Net Revenue clarity
- Supply/demand side growth balance
- Liquidity threshold timing

**Example**:
```
Category: Used car sales
Annual: 3M cars × ₩15M = ₩45 trillion
Online penetration: 20% = ₩9 trillion GMV
Take rate: 3%
→ TAM = ₩270B (Net Revenue)
```

### Consumer

**Recommended Methodology Order**:
1. Top-down (population-based)
2. Bottom-up (MAU × ARPU)
3. Value Theory (replace offline spending)

**Key Adjustments**:
- DAU/MAU engagement rate
- Monetization mix (ads + subscription + IAP)
- K-factor and viral loops

**Example**:
```
Target: 20-40 age exercisers = 1.5M
App adoption: 10% = 150K
MAU Penetration: 20% = 30K
ARPU: ₩3K/month
→ TAM = 150K × ₩3K × 12 = ₩540B
```

### B2B Enterprise

**Recommended Methodology Order**:
1. Bottom-up (Accounts × ACV)
2. Value Theory (IT budget ROI)
3. Top-down (IT category spending)

**Key Adjustments**:
- SMB/Mid/Ent segmentation
- Sales cycle length (120-270 days)
- Multi-year contracts

**Example**:
```
Target: Korea finance (banks, brokers, insurers)
Accounts: 100 (top tier only)
ACV: ₩500M/year
Win rate: 20%
5-year target: 20 customers
→ SOM = 20 × ₩500M = ₩100B
```

---

## Final Recommendations

### For Investors

**1-Page Output**:
```markdown
# Market Opportunity

TAM: $2B | SAM: $500M | SOM: $25M (5yr)

**Validated by:**
✓ Top-down (Gartner market data)
✓ Bottom-up (60K targets × $5M ARPA)
✓ Value Theory ($100K savings basis)

**Growth**: 15% annual CAGR
```

### Keep Assumptions Document

Detailed per-methodology calculation, sources, and rationale. Investors will ask.

### Update Quarterly

- Real ARPA vs assumptions
- Actual conversion vs models
- Market growth rate changes
- Competition shifts

→ Adjust TAM/SAM/SOM accordingly
