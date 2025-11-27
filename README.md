# kasparro-agentic-fb-analyst-Rohith-Nemalipuri
Hi — I’m Rohith. This repository contains my submission for the **Kasparro Agentic Facebook Performance Analyst** assignment.
It builds a small agentic system that diagnoses Facebook Ads ROAS/CTR drops and proposes creative adjustments for low-CTR campaigns.

Tested on Python 3.10 (Windows).
```bash
python -V  # must be >= 3.10

# Create & activate virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Set dataset path (PowerShell)
$env:DATA_CSV = "data/synthetic_fb_ads_undergarments.csv"

# Run analysis
python -m src.run "Analyze why ROAS dropped in the last 14 days"
```
**Data**
This project uses a synthetic e-commerce + Facebook Ads dataset containing:
	•	campaign_name
	•	adset_name
	•	date
	•	spend
	•	impressions
	•	clicks
	•	ctr
	•	purchases
	•	revenue
	•	roas
	•	creative_type
	•	creative_message
	•	audience_type
	•	platform
	•	country

Place your dataset at:
data/synthetic_fb_ads_undergarments.csv

Or override with PowerShell:
$env:DATA_CSV = "C:\path\to\your.csv"

**Config**
Configuration is stored at:
Example:
python: "3.10"
random_seed: 42
confidence_min: 0.6
use_sample_data: false

•	random_seed → ensures reproducible insights
•	confidence_min → minimum evaluator score for insight acceptance
•	use_sample_data → for optional small test CSV

**Architecture Overview**

**1. PlannerAgent**

Breaks the marketer query into structured subtasks:
	•	trend analysis
	•	audience comparison
	•	creative breakdown
	•	cluster detection
	•	hypothesis generation

Outputs a Plan (list of PlanSteps).

**2. DataAgent**

Loads CSV and returns structured summaries:
-ROAS & CTR trend
-audience_type breakdown
-creative_type breakdown
1low-CTR clusters

Used by InsightAgent + EvaluatorAgent.

**3. InsightAgent**

Produces hypothesis drafts using:
-Prompt templates
-Data summaries
-Pattern recognition

Each insight describes:
-potential cause
-pattern observed
-reasoning

**4. EvaluatorAgent**

Quantitatively validates each hypothesis:
-computes baseline vs recent metrics
-assigns:
	-status → strong_support / partial / rejected
	-confidence_final
	-impact → low / medium / high
Outputs validated hypotheses stored in reports/insights.json.

**5. CreativeGeneratorAgent**

For low-CTR clusters:
-identifies creative weaknesses
-analyzes high-performing creatives
-generates new creative ideas:
-hooks
-messages
-CTAs
-angles

Outputs are stored in reports/creatives.json.

**6. Orchestrator**

Wires all agents and produces:
-insights.json
-creatives.json
-report.md
-logs/run_logs.json

Entry point:
src/run.py

**Repository Structure**
config/
  config.yaml
data/
  synthetic_fb_ads_undergarments.csv
prompts/
  *.md templates for all agents
logs/
  run_logs.json
reports/
  insights.json
  creatives.json
  report.md
src/
  run.py
  orchestrator.py
  agents/
    planner.py
    data_agent.py
    insight_agent.py
    evaluator.py
    creative_generator.py
  utils/
    schemas.py
    io.py
    logging_utils.py
tests/
  test_evaluator.py
  
**Running the System**
$env:DATA_CSV = "data/synthetic_fb_ads_undergarments.csv"
python -m src.run "Analyze why ROAS dropped in the last 14 days"

Outputs

After running, you should have:

reports/report.md
-Human-readable summary
-ROAS/CTR explanation
-Top insights
-Creative direction suggestions

reports/insights.json

Each item includes:
-id
-summary
-dimension
-metrics (baseline vs recent)
-suspected_causes
-evidence sentences
-status / confidence / impact

reports/creatives.json

For each low-CTR cluster:
-cluster info
-problem summary
-high-performing reference examples
-new creative ideas (messages, hooks, CTAs)

logs/run_logs.json

Agent-by-agent structured JSON logs.

Observability

Every step logs a structured trace:
-agent name
-step id
-input summary
-output summary
-timestamp

Evaluators can reconstruct the entire reasoning chain.

**Release & Submission Details**
-Release tag required: v1.0
-Command used for submission:
$env:DATA_CSV = "data/synthetic_fb_ads_undergarments.csv"
python -m src.run "Analyze why ROAS dropped in the last 14 days"

Required committed files:
-reports/insights.json
-reports/creatives.json
-reports/report.md
-logs/run_logs.json
-Required PR:
-Title: self-review
-Description: includes reasoning choices & tradeoffs.

**Self-Review Notes**
This PR reviews the design of the Agentic Facebook Performance Analyst system.

- PlannerAgent: creates structured multi-step analysis plan.
- DataAgent: summarizes dataset (trend, audience, creatives, clusters).
- InsightAgent: forms hypotheses using prompt-driven reasoning.
- EvaluatorAgent: runs quantitative checks and assigns confidence levels.
- CreativeGeneratorAgent: generates new creative ideas grounded in dataset behavior.
- Orchestrator: manages execution, logging, and final report creation.

Key tradeoffs:
- Heuristic evaluation instead of causal modeling for simplicity.
- Prompt templates optimized for synthetic dataset.
- Deterministic seeds for reproducibility.




