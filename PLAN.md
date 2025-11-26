5 — High-level plan (step-by-step with priorities)

Phase A — Setup & data (1–2 hours)
Create repo and set up virtualenv, requirements.
Put the synthetic CSV in data/. If it's large, create a data/sample_fb_ads.csv with ~200 rows (script to sample).
Add config/config.yaml and a Makefile with make run, make test.

Phase B — Core agents & orchestration (3–4 hours)
Implement src/run.py CLI that loads config, seeds randomness, and invokes orchestrator.
Implement src/orchestrator.py that instantiates agents, passes data summaries (not full CSV) between agents, collects outputs and writes reports/insights.json, reports/creatives.json, reports/report.md, and logs.
Implement src/agents/* skeletons:

planner.py (decompose query)

data_agent.py (load, validate, summarize, rolling metrics)

insight_agent.py (generate hypotheses using structured prompt & rules)

evaluator.py (quantitatively validate hypotheses; compute confidence)

creative_generator.py (generate new creatives grounded in dataset messaging using template prompts and examples)

Phase C — Prompt files & reflection loops (1 hour)

Create prompts/*.md using layered format: Think → Analyze → Conclude and JSON schema expectations, plus retry logic for low-confidence.

Phase D — Validation, tests, & report (1–2 hours)

Implement tests/test_evaluator.py to check hypothesis→metric mapping.

Create sample reports/insights.json, creatives.json, report.md from a sample run.

Ensure logs exist in logs/.

Phase E — Finalize submission (30–60 minutes)

Ensure at least 3 commits with meaningful messages.

Create PR self-review with explanation of design choices.

Create tag v1.0 and push.

Add README with exact run command, commit hash, and tag.
