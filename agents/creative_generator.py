CreativeGenerator (src/agents/creative_generator.py)

-Identify campaigns with low CTR (e.g., CTR < dataset median * 0.8 or config threshold).
-For each low-CTR campaign, sample top-performing creative messages across the dataset (by CTR/ROAS) and use template prompts to produce 6 diverse creative variants (headline, body, CTA).
-Output structured JSON with campaign_name, adset_name, creative_type, recommendations list.
