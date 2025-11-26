# kasparro-agentic-fb-analyst-Rohith-Nemalipuri
Hi — I’m Rohith. This repository contains my submission for the **Kasparro Agentic Facebook Performance Analyst** assignment.
It builds a small agentic system that diagnoses Facebook Ads ROAS/CTR drops and proposes creative adjustments for low-CTR campaigns.

The system takes a marketer query (e.g.,"Analyze ROAS drop in the last 7 days") and produces:
- A structured set of **insights** (`reports/insights.json`)
- **Creative improvement ideas** (`reports/creatives.json`)
- A **human-readable diagnosis** (`reports/report.md`)
- Basic **JSON logs** for observability (`logs/run_logs.json`)

The implementation is intentionally lightweight and framework-free so you can
inspect the agents, prompts, and orchestration clearly.
---

## Quick Start

```bash
python -V  # should be >= 3.10

# 1. Create and activate a virtualenv
python -m venv .venv
# macOS / Linux:
source .venv/bin/activate
# Windows (PowerShell):
# .venv\Scripts\Activate.ps1

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the agentic analyst
export DATA_CSV=data
python src/run.py "Analyze why ROAS dropped in the last 14 days"

# Outputs:
# - reports/report.md
# - reports/insights.json
# - reports/creatives.json
# - logs/run_logs.json
```
-----------------------------------------------------------------------------------------------------------------------------------------
## Project plan

Phase A — Setup & data (1–2 hours)
- Create repo and virtualenv, install requirements.
- Place the CSV in `data/` (or create `data/sample_fb_ads.csv` for quick runs).
- Add `config/config.yaml` and `Makefile`.

Phase B — Core agents & orchestration (3–4 hours)
- Implement `src/run.py` and `src/orchestrator.py`.
- Implement agents in `src/agents/`: planner, data_agent, insight_agent, evaluator, creative_generator.

Phase C — Prompts & reflection (1 hour)
- Add `prompts/*.md` with Think → Analyze → Conclude and retry logic.

Phase D — Validation & reports (1–2 hours)
- Add `tests/test_evaluator.py`.
- Run sample, generate `reports/insights.json`, `reports/creatives.json`, `reports/report.md`.
- Save traces to `logs/`.

Phase E — Finalize submission (30–60 minutes)
- Make 3+ commits, create PR "self-review", tag `v1.0`, push, and share repo link + commit hash + run command.

