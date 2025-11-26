# Project Plan — Kasparro Agentic FB Performance Analyst
This document is the step-by-step plan I will follow to implement the assignment.

## Phase A — Setup & data (1–2 hours)
1. Create the repository and clone it locally.
2. Create a Python virtual environment:
   - `python -m venv .venv`
   - `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`)
3. Install dependencies:
   - `pip install -r requirements.txt`
4. Place the provided CSV at `data/synthetic_fb_ads_undergarments.csv`.
   - If the CSV is large, create a sample: `data/sample_fb_ads.csv` (about 200 rows) and set `use_sample_data: true` in `config/config.yaml`.
5. Add `config/config.yaml`, `Makefile`, basic `.gitignore`.

## Phase B — Core agents & orchestration (3–4 hours)
1. Implement `src/run.py` (CLI) that reads `config/config.yaml`, seeds randomness, and calls the orchestrator.
2. Implement `src/orchestrator.py` that:
   - Instantiates agents
   - Calls DataAgent to load and summarize data
   - Calls InsightAgent to produce hypotheses
   - Calls EvaluatorAgent to validate hypotheses
   - Calls CreativeGenerator to produce creative suggestions
   - Writes `reports/insights.json`, `reports/creatives.json`, `reports/report.md`, and `logs/run_trace_<ts>.json`
3. Implement agents under `src/agents/`:
   - `planner.py` — parse query and produce subtasks
   - `data_agent.py` — lazy load CSV, validate columns, produce `data_summary` (rolling averages, trends)
   - `insight_agent.py` — rule-based hypothesis generation with structured JSON output
   - `evaluator.py` — quantitative validation (deltas, thresholds, simple stats), output confidence
   - `creative_generator.py` — create 3–6 creative variants per low-CTR campaign using templates and dataset examples

## Phase C — Prompt files & reflection loops (1 hour)
1. Create `prompts/*.md` files: `planner.md`, `data_agent.md`, `insight_agent.md`, `evaluator.md`, `creative_generator.md`.
2. Each prompt file must include:
   - Goal
   - Output JSON schema
   - Think → Analyze → Conclude
   - Retry logic if confidence < `confidence_min` from config

## Phase D — Validation, tests, & report (1–2 hours)
1. Implement `tests/test_evaluator.py` using pytest and small DataFrame fixtures.
2. Run a sample run (`use_sample_data: true`) to generate the reports:
   - `reports/insights.json`
   - `reports/creatives.json`
   - `reports/report.md`
3. Verify logs saved in `logs/` as `run_trace_<ts>.json`.

## Phase E — Finalize submission (30–60 minutes)
1. Create at least three meaningful commits:
   - `git commit -m "init: repo skeleton and config"`
   - `git commit -m "feat: implement data_agent + summary"`
   - `git commit -m "feat: orchestrator + agents skeletons and sample outputs"`
2. Create a Pull Request named `self-review` describing design choices and trade-offs.
3. Tag the release:
   - `git tag -a v1.0 -m "v1.0: initial submission"`
   - `git push origin main --tags`
4. Copy the latest commit hash:
   - `git rev-parse --short HEAD`
5. Final command to produce outputs (example to include in submission):
   - `python src/run.py "Analyze ROAS drop in last 14 days"`

## Notes & checkpoints
- Keep `use_sample_data` flag in `config/config.yaml` for fast testing.
- Seed randomness in `run.py` and agents.
- Commit `reports/insights.json` and `reports/creatives.json` as evidence for submission, unless instructed otherwise.
