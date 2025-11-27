# kasparro-agentic-fb-analyst-Rohith-Nemalipuri
Hi — I’m Rohith. This repository contains my submission for the **Kasparro Agentic Facebook Performance Analyst** assignment.
It builds a small agentic system that diagnoses Facebook Ads ROAS/CTR drops and proposes creative adjustments for low-CTR campaigns.

## Quick Start

Tested on *Python 3.10 (Windows)*.
```bash
python -V  # should be >= 3.10

# create and activate venv (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

# install dependencies
pip install -r requirements.txt

# set data path (PowerShell)
$env:DATA_CSV = "data/synthetic_fb_ads_undergarments.csv"

# run main pipeline
python -m src.run "Analyze why ROAS dropped in the last 14 days"
```

## Data

This project uses a synthetic e-commerce + Facebook Ads dataset with the following columns:

- campaign_name  
- adset_name  
- date  
- spend  
- impressions  
- clicks  
- ctr  
- purchases  
- revenue  
- roas  
- creative_type  
- creative_message  
- audience_type  
- platform  
- country

Default location:
Place your dataset at:
```
data/synthetic_fb_ads_undergarments.csv
```
Or override with PowerShell:
```
$env:DATA_CSV = “C:\path\to\your.csv”
```

### Config
Configuration is stored at:
```
config/config.yaml
```
Example:
```
python: “3.10”
random_seed: 42
confidence_min: 0.6
use_sample_data: false
```
Meaning:
- random_seed → ensures reproducible insights
- confidence_min → minimum evaluator score for insight acceptance
- use_sample_data → for optional small test CSV

## Architecture Overview

## 1.PlannerAgent
Breaks the marketer query into structured subtasks:
- trend analysis
- audience comparison
- creative breakdown
- cluster detection
- hypothesis generation

Outputs a Plan.

## 2.DataAgent
Loads CSV and returns structured summaries:
- ROAS & CTR trend
- audience_type breakdown
- creative_type breakdown
- low-CTR clusters

## 3.InsightAgent
Produces hypothesis drafts using:
- prompt templates
- data summaries
- pattern recognition

## 4.EvaluatorAgent
Quantitatively validates each hypothesis with metric deltas:
- assigns status: strong_support, partial, rejected
- assigns confidence_final
- assigns impact

## 5.CreativeGeneratorAgent
For low-CTR clusters:
- detects creative weaknesses
- studies high-performing creatives
- generates new creative ideas (hooks, messages, CTAs)

## 6.Orchestrator
Wires all agents and produces:

- insights.json
- creatives.json
- report.md
- logs/run_logs.json

Entry point: 
```
src/run.py
```

**Repository Structure**
```
config/config.yaml
data/
synthetic_fb_ads_undergarments.csv
prompts/
(Markdown templates for all agents)
logs/
run_logs.json
reports/
report.md
insights.json
creatives.json
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
```
Running the System
```
$env:DATA_CSV = “data/synthetic_fb_ads_undergarments.csv”
python -m src.run “Analyze why ROAS dropped in the last 14 days”
```
or:
```
python src/run.py “Analyze ROAS trend last 7 days”
```
## Outputs
After running you should have:
**reports/report.md**
- Human-readable summary
- ROAS/CTR explanations
- Top Insights
- Creative direction suggestions

## reports/insights.json
Contains:
- id
- summary
- dimension
- metrics
- suspected_causes
- evidence
- status/condidence/impact

## reports/creatives.json
for each low-CTR cluster:
- cluster info
- problem summary
- high-performing reference examples
- new creative ideas(messages,hooks,CTAs)

## logs/run_logs.json
Structured log for each agent execution.

Observability
System logs every step with:
- agent name
- step ID
- input summary
- output summary
- timestamp
Allows evaluation of reasoning flow.

## Release & Submission
Tag for submission: 
```
v1.0
```

## Run command used:
```
$env:DATA_CSV = “data/synthetic_fb_ads_undergarments.csv”
python -m src.run “Analyze why ROAS dropped in the last 14 days”
```
Committed files required:
- reports/insights.json
- reports/creatives.json
- reports/report.md
- logs/run_logs.json

## PR required:
Title: self-review
Contains design rationale.

## Self-Review Notes

This PR reviews the design of the Agentic Facebook Performance Analyst system.
- **PlannerAgent**: creates structured multi-step analysis plan.
- **DataAgent**: summarizes dataset (trend, audience, creatives, clusters).
- **InsightAgent**: forms hypotheses using prompt-driven reasoning.
- **EvaluatorAgent**: runs quantitative checks and assigns confidence levels.
- **CreativeGeneratorAgent**: generates new creative ideas grounded in dataset behavior.
- Orchestrator: manages execution, logging, and final report creation.

Tradeoffs:
- Simple statistical evaluation instead of causal models
- Prompts tuned for synthetic dataset
- Deterministic seeds for reproducibility

