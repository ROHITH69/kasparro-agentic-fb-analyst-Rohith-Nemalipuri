# Data — Synthetic Facebook Ads (Undergarments)
This folder contains the **synthetic** Facebook ads dataset used by the
agentic performance analyst.

## Files
- `synthetic_fb_ads_undergarments.csv`  
  4500 rows, daily performance over 90 days (`2025-01-01` to `2025-03-31`).

## Schema
Columns:
- `campaign_name` (str)
- `adset_name` (str)
- `date` (YYYY-MM-DD)
- `spend` (float)
- `impressions` (int)
- `clicks` (float)
- `ctr` (float) — click-through rate (clicks / impressions)
- `purchases` (int)
- `revenue` (float)
- `roas` (float) — return on ad spend (revenue / spend)
- `creative_type` (str) — e.g., Image, Video, Carousel, UGC
- `creative_message` (str) — ad copy text
- `audience_type` (str) — Broad, Lookalike, Retargeting
- `platform` (str) — Facebook, Instagram
- `country` (str) — e.g., US, IN

## Usage
The analyst loads the CSV and:

- Compares **first 14 days vs last 14 days** for ROAS, CTR, and purchases/day.
- Computes metrics by **audience_type** and **creative_type**.
- Identifies low-CTR, low-ROAS **campaign+adset clusters** to target with
  creative improvements.

By default, `config/config.yaml` points here, but you can override via:
```bash
export DATA_CSV="kasparro-agentic-fb-analyst-Rohith-Nemalipuri/data/synthetic_fb_ads_undergarments.csv"

