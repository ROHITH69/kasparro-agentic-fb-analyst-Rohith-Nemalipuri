# kasparro-agentic-fb-analyst-Rohith-Nemalipuri
Hi — I’m Rohith. This repository contains my submission for the **Kasparro Agentic Facebook Performance Analyst** assignment.
It builds a small agentic system that diagnoses Facebook Ads ROAS/CTR drops and proposes creative adjustments for low-CTR campaigns.

---
## Quick start (run locally)

Requirements:
- Python 3.10+
- Create and activate a virtualenv

```bash
python -m venv .venv
# mac/linux
source .venv/bin/activate
# windows (powershell)
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
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
