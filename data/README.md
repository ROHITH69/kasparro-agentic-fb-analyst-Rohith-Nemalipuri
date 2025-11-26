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
export DATA_CSV="data/synthetic_fb_ads_undergarments.csv"
```
--------------------------------------------------------------------------------------------------------------------------------
## Configuration

All tunable behaviour is controlled via `config/config.yaml` — nothing is hardcoded in the code.
Key sections:

- `data`  
  - `csv_path`: default location of the synthetic FB ads dataset.  
    If the `DATA_CSV` environment variable is set, it overrides this path.  
  - `date_column`: name of the date column in the CSV.

- `windows`  
  - `baseline_days` and `comparison_days`: how many days are used for the
    “before vs after” ROAS comparison (e.g. first 14 vs last 14 days).

- `run`  
  - `random_seed`: global seed used for any sampling/shuffling and creative
    variation, so runs are reproducible.

- `thresholds`  
  - `min_impressions`, `min_spend`, `min_purchases`: minimum volume required
    for a campaign/adset cluster to be included in insights (prevents noise
    from tiny segments).  
  - `roas_drop_pct_strong`, `roas_drop_pct_partial`: ROAS change thresholds
    used by the Evaluator Agent to classify a hypothesis as `strong_support`,
    `partial`, or `rejected`.  
  - `low_ctr_pct_below_account`: how far below the account-wide CTR a cluster
    must be to be flagged as “low CTR” and passed to the Creative Generator.

The agents (DataAgent, InsightAgent, EvaluatorAgent, CreativeGenerator) all
read these values from `config/config.yaml`. To change behaviour, update the
YAML file — no code changes are required.
