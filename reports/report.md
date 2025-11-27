# ROAS Diagnostic Report
This report summarizes ROAS and CTR changes, validated insights, and creative recommendations.

- ROAS dropped mainly due to audience fatigue in Retargeting groups.
- CTR decreased for Static Image creatives after 10+ days.
- Evaluator confirmed CTR drop with -32% week-over-week change.

See insights.json and creatives.json for structured outputs.

**Query:**
Analyze why ROAS dropped in the last 14 days

## 1. Executive Summary
- ROAS dropped from **6.10** to **5.37** (~**-12.0%**).
- CTR shifted from **1.32%** to **1.21%** (~**-8.5%**).
- Purchases per day changed from **3975** to **3584** (~**-9.8%**).
Overall, the account is seeing slightly fewer clicks per impression and slightly
weaker conversion efficiency at similar spend, leading to a ~12% ROAS decline.

## 2. Key Insights
### H1_roas_trend_last_14_vs_first_14

- **Summary:** Account-level ROAS in the last 14 days is lower than in the first 14 days.
- **Dimension:** `date`
- **Status:** `strong_support`
- **Confidence:** 0.85 | **Impact:** high
- **Evidence:**
  - Mean ROAS changed from 6.10 to 5.37.
  - CTR changed from 1.32% to 1.21%.
  - Purchases per day changed from 3975 to 3584.
- **Suspected causes:**
  - creative_fatigue
  - slightly weaker CTR and conversion rate at similar spend

### H2_retarg_outperforms_broad

- **Summary:** Retargeting audiences deliver significantly higher ROAS than Broad at similar CTR.
- **Dimension:** `audience_type`
- **Status:** `partial`
- **Confidence:** 0.70 | **Impact:** medium
- **Evidence:**
  - Retargeting ROAS is 9.33 vs Broad 5.00.
  - CTR is similar (1.22%–1.30%), so better conversion rate likely drives the ROAS gap.
- **Suspected causes:**
  - warmer audiences
  - higher intent users in retargeting pools

### H3_video_underperforms_static

- **Summary:** Video creatives underperform static formats (Image/Carousel) on ROAS and CTR.
- **Dimension:** `creative_type`
- **Status:** `partial`
- **Confidence:** 0.70 | **Impact:** medium
- **Evidence:**
  - Video ROAS is 5.35 vs Image 6.13 and Carousel 6.18.
  - Video CTR is 1.18% vs UGC 1.34%.
- **Suspected causes:**
  - weak hooks in first seconds of video
  - less product clarity vs static formats

### H4_low_ctr_clusters_drag_down_blended

- **Summary:** Several campaign+adset clusters have CTR far below the account average while spending meaningful budget.
- **Dimension:** `campaign_name+adset_name`
- **Status:** `strong_support`
- **Confidence:** 0.88 | **Impact:** high
- **Evidence:**
  - Account-wide CTR is ~1.27%, but some clusters sit around 0.56%–0.61%.
  - Each of these clusters spends between 2.6k and 4.7k.
- **Suspected causes:**
  - generic messaging that fails to stand out
  - creative fatigue on repeated "seamless everyday" angle

## 3. Recommended Next Steps
- Pause or refactor the lowest-CTR, lowest-ROAS Women Seamless Everyday clusters.
- Protect and gradually scale high-ROAS retargeting audiences with fresh creatives.
- Overhaul video hooks to match the best-performing static angles.
- Re-run this analysis weekly to track whether fixes close the ROAS gap.
