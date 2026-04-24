# Financial Model Templates by Business Model

This document provides detailed financial model templates for 4 major business models (SaaS, Marketplace, E-commerce, Services). Each template includes monthly structure, core drivers, spreadsheet formulas, and real-world examples.

---

## Table of Contents

1. [SaaS Financial Model](#saas-financial-model)
2. [Marketplace Financial Model](#marketplace-financial-model)
3. [E-commerce Financial Model](#e-commerce-financial-model)
4. [Services/Agency Financial Model](#servicesagency-financial-model)

---

## SaaS Financial Model

### Core Drivers

**Revenue Composition:**
```
MRR (Monthly Recurring Revenue) =
  Prior Month MRR
  + New MRR (new customers)
  + Expansion MRR (upsell/cross-sell)
  - Contraction MRR (downgrades)
  - Churn MRR (cancellations)

ARR = MRR × 12
```

**Unit Economics:**
```
CAC = (S&M Spend) / (New Customers)
LTV = (ARPU × Gross Margin) / Churn Rate
CAC Payback = CAC / (ARPU × Gross Margin)
```

**Core Metrics:**
- Net Revenue Retention (NRR)
- Gross Revenue Retention (GRR)
- Rule of 40 = Growth Rate + EBITDA Margin
- Magic Number = (Net New ARR) / (S&M Spend)

### Monthly Structure

#### Sheet 1: Customers & MRR Buildup

```
| Month | M1 | M2 | M3 | ... | M36 |
|-------|----|----|----|----|-----|
| **Customer Count** |
| Prior Month | 0 | =B2+B3-B5 | =C2+C3-C5 | ... |
| New Customers | 10 | 12 | 15 | ... | 150 |
| Upgrades | 0 | 0 | 1 | ... | 20 |
| Downgrades | 0 | 0 | 0 | ... | 5 |
| Churn | 0 | 0 | 1 | ... | 15 |
| End of Month | 10 | =B2+B3-B5 | ... | ... |
|  |
| **MRR Buildup** |
| Prior Month MRR | 0 | =B9+B10-B11-B12 | ... |
| New MRR | 1,000 | 1,200 | 1,500 | ... | 15,000 |
| Expansion MRR | 0 | 0 | 100 | ... | 3,000 |
| Contraction MRR | 0 | 0 | 0 | ... | 200 |
| Churn MRR | 0 | 0 | 100 | ... | 1,500 |
| End of Month MRR | 1,000 | =B9+B10-B11-B12 | ... | ... |
|  |
| **Metrics** |
| ARPU | =B13/B6 | =C13/C6 | ... |
| Gross Churn % | - | =C12/C9 | ... |
| Net Churn % | - | =(C12-C11)/C9 | ... |
| NRR % | - | =(C9+C11-C12)/B9 | ... |
```

#### Sheet 2: Cohort Analysis

```
Customer Cohorts (Monthly):

|        | M0   | M1   | M2   | M3   | ... | M12  |
|--------|------|------|------|------|-----|------|
| Jan-24 | 100% | 97%  | 94%  | 92%  | ... | 75%  |
| Feb-24 | 100% | 96%  | 93%  | 91%  | ... | 74%  |
| Mar-24 | 100% | 97%  | 95%  | 93%  | ... | 76%  |

MRR Cohorts (Monthly MRR):

|        | M0    | M1    | M2    | M3    | ... | M12   |
|--------|-------|-------|-------|-------|-----|-------|
| Jan-24 | $10K  | $10.5K| $11K  | $11.2K| ... | $14K  |
| Feb-24 | $12K  | $12.6K| $13K  | $13.5K| ... | $17K  |
| Mar-24 | $15K  | $15.8K| $16.5K| $17K  | ... | $21K  |

Interpretation:
- M0 → M12 Retention: 75% (Target: >80%)
- M0 → M12 MRR Expansion: 140% (due to expansion)
- NRR = 140% × 75% = 105% (>100% = healthy)
```

#### Sheet 3: P&L Statement

```
| Month | M1 | M2 | M3 | ... | M36 |
|-------|----|----|----|----|-----|
| **Revenue** |
| MRR | 1,000 | =Sheet1!B13 | ... |
| Setup Fee | 100 | 120 | 150 | ... |
| Total Revenue | =B2+B3 | =C2+C3 | ... |
|  |
| **COGS** |
| Hosting (20% of MRR) | -200 | =C2*0.2 | ... |
| API Costs (5%) | -50 | =C2*0.05 | ... |
| CS (per customer $5) | =-Sheet1!B6*5 | ... |
| Total COGS | =SUM(B6:B8) | ... |
| Gross Profit | =B4+B9 | ... |
| Gross Margin % | =B10/B4 | ... |
|  |
| **Operating Expenses** |
| R&D | -5,000 | -5,500 | -6,000 | ... |
| Sales & Marketing | -3,000 | -3,500 | -4,000 | ... |
| G&A | -1,000 | -1,200 | -1,500 | ... |
| Total OpEx | =SUM(B13:B15) | ... |
|  |
| **EBITDA** | =B10+B16 | ... |
| EBITDA Margin % | =B18/B4 | ... |
```

### Example: SaaS Startup (Base Scenario)

**Assumptions:**
- Starting customers: 0
- New customers/month: M1-M12: 10→50 (linear growth), M13-M36: 50→150
- ARPU: $100 (M1-M12), $120 (M13-M36 — price increase)
- Churn: 3.5%/month
- Expansion: 15% of customers upgrade annually (+50% ARPU)
- CAC: $300
- Gross Margin: 75%

**Results (Year 3 End):**
- Customer count: 2,500
- MRR: $300K
- ARR: $3.6M
- NRR: 105%
- LTV:CAC: 3.4:1
- CAC Payback: 8.5 months
- Rule of 40: 60% (45% growth + 15% EBITDA)

---

## Marketplace Financial Model

### Core Drivers

**Revenue Composition:**
```
GMV (Gross Merchandise Value) = Transaction Volume × Avg Transaction Amount
Revenue = GMV × Take Rate
```

**Two-Sided Growth:**
```
Supply: Seller count, listing count
Demand: Buyer count, transaction count
Liquidity = Transaction completion rate
```

**Unit Economics:**
```
CAC (Buyer) = (Marketing Spend) / (New Buyers)
CAC (Seller) = (Seller acquisition cost) / (New Sellers)
LTV (Buyer) = (Avg transaction frequency × Avg transaction amount × Take Rate) / Churn
```

### Monthly Structure

#### Sheet 1: Supply/Demand & GMV

```
| Month | M1 | M2 | M3 | ... | M36 |
|-------|----|----|----|----|-----|
| **Supply** |
| Active Sellers | 50 | 60 | 72 | ... | 1,000 |
| New Sellers | 50 | 15 | 18 | ... | 100 |
| Seller Churn | 0 | 5 | 6 | ... | 80 |
| Listings per Seller | 5 | 6 | 7 | ... | 10 |
| Total Listings | =B2*B5 | ... |
|  |
| **Demand** |
| Active Buyers | 200 | 250 | 310 | ... | 5,000 |
| New Buyers | 200 | 80 | 100 | ... | 500 |
| Buyer Churn | 0 | 30 | 40 | ... | 400 |
| Transactions per Buyer/mo | 0.5 | 0.6 | 0.7 | ... | 1.2 |
|  |
| **GMV & Revenue** |
| Total Transactions | =B8*B11 | ... |
| Avg Transaction Amount | $50 | $52 | $54 | ... | $80 |
| GMV | =B13*B14 | ... |
| Take Rate | 15% | 16% | 17% | ... | 20% |
| Revenue | =B15*B16 | ... |
|  |
| **Liquidity Metrics** |
| Transactions per Listing | =B13/B6 | ... |
| Transaction Completion Rate | - | 10% | 12% | ... | 25% |
| Repeat Purchase Rate | - | 30% | 35% | ... | 60% |
```

#### Sheet 2: P&L Statement

```
| Month | M1 | M2 | M3 | ... | M36 |
|-------|----|----|----|----|-----|
| **Revenue** |
| GMV | =Sheet1!B15 | ... |
| Take Rate | =Sheet1!B16 | ... |
| Total Revenue | =Sheet1!B17 | ... |
|  |
| **COGS** |
| Payment Processing (2.9%) | =B2*0.029 | ... |
| Fraud Prevention | =B2*0.005 | ... |
| CS (per transaction $0.5) | =-Sheet1!B13*0.5 | ... |
| Total COGS | =SUM(B6:B8) | ... |
| Gross Profit | =B4+B9 | ... |
| Gross Margin % | =B10/B4 | ... |
|  |
| **Operating Expenses** |
| R&D | -10,000 | -11,000 | ... |
| S&M (Buyers) | =Sheet1!B9*CAC_buyer | ... |
| S&M (Sellers) | =Sheet1!B3*CAC_seller | ... |
| G&A | -2,000 | -2,200 | ... |
| Total OpEx | =SUM(B13:B16) | ... |
|  |
| **EBITDA** | =B10+B17 | ... |
```

### Example: Marketplace (Base Scenario)

**Assumptions:**
- Starting: 50 sellers, 200 buyers
- Growth: Sellers +20%/month (M1-M12) → +10%/month (M13-M36)
- Growth: Buyers +25%/month (M1-M12) → +15%/month (M13-M36)
- Avg transaction amount: $50 (M1) → $80 (M36)
- Take Rate: 15% (M1) → 20% (M36 — brand strengthening)
- Buyer CAC: $20
- Seller CAC: $100

**Results (Year 3 End):**
- GMV: $4M/month
- Revenue: $800K/month (20% Take Rate)
- Active Sellers: 1,000
- Active Buyers: 5,000
- Gross Margin: 65%
- Liquidity: 0.4 transactions per listing/month

---

## E-commerce Financial Model

### Core Drivers

**Revenue Composition:**
```
GMV = Order Count × AOV (Average Order Value)
Revenue = GMV (own inventory) or GMV × Take Rate (marketplace model)
```

**Customer Cohorts:**
```
New customers: First purchase
Repeat customers: 2+ purchases
LTV = Avg lifetime order count × AOV × Gross Margin
```

**Inventory Management:**
```
Inventory Turnover = COGS / Avg Inventory
Cash Conversion Cycle = Days Inventory Held + Days Receivables - Days Payable
```

### Monthly Structure

#### Sheet 1: Orders & GMV

```
| Month | M1 | M2 | M3 | ... | M36 |
|-------|----|----|----|----|-----|
| **Customer Acquisition** |
| Month Start | 0 | =B2+B3-B4 | ... |
| New Customers | 500 | 600 | 720 | ... | 5,000 |
| Churn | 0 | 50 | 60 | ... | 500 |
| Month End | =B2+B3-B4 | ... |
|  |
| **Orders & GMV** |
| New Customer Orders | =B3*1.0 | ... | # 1.0 = first purchase rate |
| Repeat Orders | =B2*0.3 | ... | # 0.3 = monthly repeat rate |
| Total Orders | =B7+B8 | ... |
|  |
| New Customer AOV | $60 | $62 | $64 | ... | $100 |
| Repeat Customer AOV | - | $80 | $85 | ... | $150 |
| Blended AOV | =IF(B9=0,B11,(B7*B11+B8*B12)/B9) | ... |
| GMV | =B9*B13 | ... |
|  |
| **Repeat Metrics** |
| Repeat Rate | - | =B8/(B2+B3) | ... |
| Cohort LTV (12mo) | - | - | ... | $450 |
```

#### Sheet 2: Inventory & COGS

```
| Month | M1 | M2 | M3 | ... | M36 |
|-------|----|----|----|----|-----|
| **Inventory Management** |
| Month Start | 10,000 | =B2+B3-B4 | ... |
| Purchases | 20,000 | 25,000 | 30,000 | ... |
| COGS | =-Sheet1!B14*0.55 | ... | # 55% COGS |
| Month End | =B2+B3+B4 | ... |
|  |
| Inventory Turnover (Annual) | =(-B4*12)/((B2+B5)/2) | ... |
| Days Inventory | =365/B7 | ... |
```

#### Sheet 3: P&L Statement

```
| Month | M1 | M2 | M3 | ... | M36 |
|-------|----|----|----|----|-----|
| **Revenue** |
| GMV | =Sheet1!B14 | ... |
| Total Revenue | =B2 | ... | # Own inventory model |
|  |
| **COGS** |
| Product Cost (55%) | =Sheet2!B4 | ... |
| Shipping (per order $5) | =-Sheet1!B9*5 | ... |
| Inventory Management (3% of GMV) | =-B2*0.03 | ... |
| Total COGS | =SUM(B6:B8) | ... |
| Gross Profit | =B3+B9 | ... |
| Gross Margin % | =B10/B3 | ... |
|  |
| **Operating Expenses** |
| R&D | -5,000 | -5,500 | ... |
| S&M (CAC $30) | =-Sheet1!B3*30 | ... |
| G&A | -2,000 | -2,200 | ... |
| Total OpEx | =SUM(B13:B15) | ... |
|  |
| **EBITDA** | =B10+B16 | ... |
```

### Example: E-commerce (Base Scenario)

**Assumptions:**
- New customers/month: 500 (M1) → 5,000 (M36)
- First purchase rate: 100% (given)
- Repeat purchase rate: 30%/month (active customers)
- New Customer AOV: $60 → $100 (3 years)
- Repeat Customer AOV: $80 → $150 (3 years)
- COGS: 55% of GMV
- CAC: $30
- Shipping: $5/order

**Results (Year 3 End):**
- GMV: $600K/month
- Order count: 6,000/month
- Blended AOV: $100
- Gross Margin: 42%
- Repeat customer %: 60%
- LTV: $450 (12 months)
- LTV:CAC: 15:1

---

## Services/Agency Financial Model

### Core Drivers

**Revenue Composition:**
```
Time-based:
Revenue = Billable Headcount × Hourly Billing Rate × Utilization Rate × Working Hours

Project-based:
Revenue = Project Count × Avg Project Size
```

**Headcount Planning:**
```
Billable Ratio = Billable Staff / Total Staff
Utilization Rate = Actual Billable Hours / Available Hours
```

**Productization Transition:**
```
Services Revenue → Product Revenue ratio change
Services Gross Margin: 40-50%
Product Gross Margin: 70-80%
```

### Monthly Structure

#### Sheet 1: Headcount & Time-based Revenue

```
| Month | M1 | M2 | M3 | ... | M36 |
|-------|----|----|----|----|-----|
| **Headcount Planning** |
| Total HC | 10 | 11 | 12 | ... | 50 |
| - Senior (billing $150/h) | 3 | 3 | 4 | ... | 15 |
| - Mid (billing $100/h) | 4 | 5 | 5 | ... | 20 |
| - Junior (billing $60/h) | 3 | 3 | 3 | ... | 15 |
|  |
| Non-billable (Mgmt, Sales) | 2 | 2 | 3 | ... | 10 |
| Billable HC | =B2-B6 | ... |
| Billable % | =B7/B2 | ... |
|  |
| **Hours & Utilization** |
| Available Hours/Person/mo | 160 | 160 | 160 | ... |
| Utilization Rate | 65% | 70% | 75% | ... | 80% |
| Billable Hours/Person/mo | =B10*B11 | ... |
|  |
| **Time-based Revenue** |
| Senior Revenue | =B3*B12*150 | ... |
| Mid Revenue | =B4*B12*100 | ... |
| Junior Revenue | =B5*B12*60 | ... |
| Total Time Revenue | =SUM(B14:B16) | ... |
```

#### Sheet 2: Project-based Revenue

```
| Month | M1 | M2 | M3 | ... | M36 |
|-------|----|----|----|----|-----|
| **Project Pipeline** |
| New Projects | 3 | 4 | 5 | ... | 15 |
| In Progress | 3 | 5 | 7 | ... | 30 |
| Completed | 0 | 2 | 3 | ... | 12 |
|  |
| **Project Revenue** |
| Avg Project Size | $30K | $35K | $40K | ... | $80K |
| Project Duration (mo) | 2 | 2 | 2.5 | ... | 3 |
| Monthly Revenue Recognized | =B2*B6/B7 | ... |
|  |
| **Product Revenue (Transition)** |
| Product MRR | 0 | 0 | 1,000 | ... | 50,000 |
```

#### Sheet 3: P&L Statement

```
| Month | M1 | M2 | M3 | ... | M36 |
|-------|----|----|----|----|-----|
| **Revenue** |
| Time-based | =Sheet1!B17 | ... |
| Project-based | =Sheet2!B8 | ... |
| Product (SaaS) | =Sheet2!B11 | ... |
| Total Revenue | =SUM(B2:B4) | ... |
|  |
| **COGS (Labor)** |
| Senior Salary ($10K/mo per person) | =-Sheet1!B3*10000 | ... |
| Mid Salary ($6K/mo per person) | =-Sheet1!B4*6000 | ... |
| Junior Salary ($4K/mo per person) | =-Sheet1!B5*4000 | ... |
| Product COGS (20%) | =-B4*0.2 | ... |
| Total COGS | =SUM(B7:B10) | ... |
| Gross Profit | =B5+B11 | ... |
| Gross Margin % | =B12/B5 | ... |
|  |
| **Operating Expenses** |
| Non-billable Salaries | =-Sheet1!B6*12000 | ... |
| S&M | -5,000 | -6,000 | ... |
| G&A | -3,000 | -3,300 | ... |
| Total OpEx | =SUM(B15:B17) | ... |
|  |
| **EBITDA** | =B12+B18 | ... |
```

### Example: Services → SaaS Transition (Base Scenario)

**Assumptions:**
- Starting team: 10 (8 billable)
- Growth: +2/quarter (M1-M24), +5/quarter (M25-M36)
- Utilization: 65% (M1-M6) → 80% (M36)
- Average billing rate: $100/h (weighted avg)
- Projects: 3/month (M1) → 15/month (M36)
- Avg project size: $30K → $80K
- Product transition: Start M12, 40% of revenue by M36

**Results (Year 3 End):**
- Total Revenue: $500K/month
  - Services: $300K (60%)
  - Product (SaaS): $200K (40%)
- Headcount: 50 (35 billable)
- Gross Margin:
  - Services: 45%
  - Product: 80%
  - Blended: 59%
- EBITDA Margin: 15%

---

## Spreadsheet Formula Cheat Sheet

### Common Formulas

**MRR Buildup:**
```
=Prior_MRR + New_MRR + Expansion_MRR - Contraction_MRR - Churn_MRR
```

**Churn Rate:**
```
=Churn_Customers / Month_Start_Customers
=Churn_MRR / Month_Start_MRR
```

**NRR (Net Revenue Retention):**
```
=(Month_Start_MRR + Expansion_MRR - Churn_MRR) / Month_Start_MRR
```

**CAC Payback (months):**
```
=CAC / (ARPU * Gross_Margin)
```

**LTV:**
```
=(ARPU * Gross_Margin) / Churn_Rate
```

**LTV:CAC Ratio:**
```
=LTV / CAC
```

**Gross Margin %:**
```
=(Revenue - COGS) / Revenue
```

**EBITDA Margin %:**
```
=EBITDA / Revenue
```

**Burn Multiple:**
```
=(Net_Cash_Burn) / (Net_New_ARR)
```
Lower is better (1x = burn $1 to create $1 ARR)

**Rule of 40:**
```
=YoY_Growth_Rate + EBITDA_Margin
```
40%+ = healthy

**Magic Number (SaaS):**
```
=(Current_Quarter_Net_New_ARR) / (Prior_Quarter_S&M_Spend)
```
1.0+ = efficient

### Cohort Retention Calculation

**Monthly Retention:**
```
Cohort_M1 = (M1_Active_Customers / M0_Active_Customers)
Cohort_M2 = (M2_Active_Customers / M0_Active_Customers)
...
```

**Dollar Retention:**
```
Cohort_M1_MRR = M1_Cohort_MRR
```

### Growth Rate Calculations

**MoM Growth Rate:**
```
=(Current_Month / Prior_Month) - 1
```

**CAGR (Compound Annual Growth Rate):**
```
=((Ending_Value / Beginning_Value)^(1/Years)) - 1
```

---

## Benchmarks & Target Setting

### SaaS Benchmarks (By Stage)

| Metric | Seed | Series A | Series B |
|--------|------|----------|----------|
| ARR | $0.5-2M | $3-10M | $10-30M |
| YoY Growth | 100%+ | 80-100% | 60-80% |
| Gross Margin | 60-70% | 70-75% | 75-80% |
| Net Churn | <10% | <5% | <5% |
| NRR | 95-105% | 105-110% | 110-120% |
| CAC Payback | <18mo | <12mo | <9mo |
| LTV:CAC | 2:1+ | 3:1+ | 4:1+ |
| Rule of 40 | 40+ | 50+ | 60+ |

### Marketplace Benchmarks

| Metric | Early | Growth | Scale |
|--------|-------|--------|-------|
| GMV | $1-5M | $10-50M | $100M+ |
| Take Rate | 10-15% | 15-20% | 20-25% |
| Gross Margin | 50-60% | 60-70% | 70-75% |
| Liquidity | 10-15% | 20-30% | 30-40% |
| Repeat Tx % | 20-30% | 40-50% | 60-70% |

### E-commerce Benchmarks

| Metric | Early | Growth | Scale |
|--------|-------|--------|-------|
| GMV | $0.5-2M | $5-20M | $50M+ |
| Gross Margin | 35-45% | 40-50% | 45-55% |
| Repeat Rate | 20-30% | 35-45% | 50-60% |
| LTV:CAC | 5:1+ | 8:1+ | 10:1+ |
| AOV | $50-80 | $80-120 | $120-200 |

---

## Scenario Design Guidelines

### Base Scenario (50-60% probability)

**Principles:**
- Realistic and achievable
- Based on market average or benchmarks
- Reflect known risks (exclude severe shocks)

**Example Assumptions:**
- SaaS: +10-15%/mo MRR growth, 3.5% churn
- Marketplace: +15-20%/mo GMV growth, Take Rate 15%→18%
- E-commerce: +20%/mo order growth, 30% repeat rate

### Bull Scenario (20-30% probability)

**Principles:**
- Everything goes well
- Top 25% benchmark
- Strong product-market fit, successful channel optimization

**Example Assumptions:**
- SaaS: +20-25%/mo MRR growth, 2% churn
- Marketplace: +30%/mo GMV growth, Take Rate 18%→22%
- E-commerce: +35%/mo order growth, 45% repeat rate

### Bear Scenario (10-20% probability)

**Principles:**
- Key risks materialize
- Market slowdown, intensified competition, execution challenges
- Difficult but not worst-case

**Example Assumptions:**
- SaaS: +5%/mo MRR growth, 6% churn
- Marketplace: +8%/mo GMV growth, Take Rate flat at 15%
- E-commerce: +10%/mo order growth, 20% repeat rate

---

## Additional Resources

**External Benchmark Sources:**
- OpenView SaaS Benchmarks
- Bessemer Cloud Index
- Andreessen Horowitz Marketplace Metrics
- FirstRound Capital State of Startups

**Model Validation Checklist:**
- [ ] Are all formulas correct?
- [ ] Is cohort retention realistic?
- [ ] CAC Payback < 18 months?
- [ ] LTV:CAC > 3:1?
- [ ] Gross Margin within benchmark range?
- [ ] Sufficient runway? (minimum 12 months)
- [ ] Bull/Bear scenarios reasonable?
- [ ] Assumptions documented?

**Next Steps:**
1. Select template matching your business model
2. Input current state data
3. Set scenario-specific assumptions
4. Generate 3-5 year forecast
5. Create charts for investor presentation
6. Update model monthly based on actual results
