DataAgent (src/agents/data_agent.py)

-Load CSV lazily (pandas).
-Validate columns present (list in assignment).
-Return data_summary: aggregated metrics by campaign/adset/date:
  last_7/14/30 day ROAS, CTR, impressions trend slope, spend.
  ABR: rolling averages and % change.
  top creatives with CTR and ROAS.
-Keep self.dataframe for Evaluator access but do not pass full CSV into prompts; pass summaries.
