# Facebook Performance Diagnosis

**Query:** Analyze why ROAS dropped in the last 14 days

## 1. Executive Summary

- ROAS dropped from **6.10** to **5.37** (~-12.0% change).

- CTR shifted from **1.32%** to **1.21%** (~-8.5% change).

- Purchases per day changed from **3975** to **3584** (~-9.8% change).


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

- **Confidence:** 0.90 | **Impact:** medium

- **Suspected causes:**
  - warmer audiences
  - higher intent users in retargeting pools

### H3_video_underperforms_static

- **Summary:** Video creatives underperform static formats (Image/Carousel) on ROAS and CTR.

- **Dimension:** `creative_type`

- **Status:** `partial`

- **Confidence:** 0.70 | **Impact:** medium

- **Suspected causes:**
  - weak hooks in first seconds of video
  - less product clarity vs static formats

### H4_low_ctr_clusters_drag_down_blended

- **Summary:** Several campaign+adset clusters have CTR far below the account average while spending meaningful budget.

- **Dimension:** `campaign_name+adset_name`

- **Status:** `partial`

- **Confidence:** 0.85 | **Impact:** medium

- **Suspected causes:**
  - generic messaging that fails to stand out
  - creative fatigue on repeated angles

## 3. Recommended Next Steps

- Pause or refactor the worst low-CTR clusters.
- Protect and refresh high-ROAS retargeting audiences.
- Rebuild video creatives with stronger hooks and product clarity.
- Re-run this agentic analysis weekly to track changes.
