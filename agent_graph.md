# Agent Graph — Kasparro Agentic Facebook Performance Analyst

## High-Level Flow

User query  
→ **PlannerAgent**  
→ **DataAgent**  
→ **InsightAgent**  
→ **EvaluatorAgent**  
→ **CreativeGeneratorAgent**  
→ final outputs in `reports/` and `logs/`.

## Text Diagram

PlannerAgent
  ├── DataAgent
  │     └── produces `DataSummaries`
  │           (ROAS/CTR trends, audience segments, creative breakdown, low-CTR clusters)
  ├── InsightAgent
  │     └── produces `HypothesisDraft` list
  ├── EvaluatorAgent
  │     └── produces `ValidatedHypothesis` list
  └── CreativeGeneratorAgent
        └── produces `CreativeRecommendation` list
        
Orchestrator wires the agents together:

1. **PlannerAgent**
   - Takes the user query (e.g. "Analyze why ROAS dropped in the last 14 days").
   - Breaks it into steps: trend analysis, audience comparison, creative analysis, cluster inspection.

2. **DataAgent**
   - Loads the CSV from `DATA_CSV` (or `data/synthetic_fb_ads_undergarments.csv`).
   - Computes summaries per time slice, audience_type, creative_type, and low-CTR clusters.
   - Returns structured `DataSummaries` objects.

3. **InsightAgent**
   - Reads `DataSummaries`.
   - Uses prompt templates to draft hypotheses (what might be driving ROAS/CTR changes).
   - Outputs `HypothesisDraft` objects.

4. **EvaluatorAgent**
   - Quantitatively validates each hypothesis using metric deltas from the summaries.
   - Assigns:
     - `status` (strong_support | partial | rejected)
     - `confidence_final` (0–1)
     - `impact` (low | medium | high)
   - Produces `ValidatedHypothesis` objects written to `reports/insights.json`.

5. **CreativeGeneratorAgent**
   - Focuses on low-CTR clusters identified by `DataAgent` and filtered by `EvaluatorAgent`.
   - Uses high-performing creative messages as references.
   - Generates new hooks/messages/CTAs.
   - Writes recommendations to `reports/creatives.json`.

6. **Orchestrator (src/run.py + src/orchestrator.py)**
   - Executes the full plan end-to-end.
   - Logs each step into `logs/run_logs.json`.
   - Writes the human-readable `reports/report.md` summary.
