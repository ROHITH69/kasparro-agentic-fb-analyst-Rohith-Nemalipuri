EvaluatorAgent (src/agents/evaluator.py)

-Input: hypotheses, full df
-Quantitatively test each hypothesis via checks (z-scores, relative drops > threshold, cross-validation of metrics).
-Output truth score/confidence and evidence dict (metric deltas, p-values optionally).
-Add confidence based on statistical checks and rule heuristics. If low confidence, instruct InsightAgent to retry/refine.
