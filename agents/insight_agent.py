InsightAgent (src/agents/insight_agent.py)

-Input: data_summary + plan
-Apply structured reasoning to produce hypotheses, e.g.:
  audience_fatigue (evidence: impressions up, CTR down, frequency up)
  creative_underperformance (evidence: older creative age, low CTR relative to baseline)
  bid/auction change (if CPC/spend patterns change)
-For each hypothesis produce:
  id, title, description, required_evidence (metrics to check), initial_confidence (rule-based), evidence_summary (string).
