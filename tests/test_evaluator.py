from src.agents.evaluator import EvaluatorAgent

def test_evaluator_sets_strong_support_for_large_roas_drop():
    config = {}
    evaluator = EvaluatorAgent(config=config)

    hyp = {
        "id": "H1_roas_trend_last_14_vs_first_14",
        "summary": "Test roas trend.",
        "dimension": "date",
        "metrics": {
            "roas_baseline": 10.0,
            "roas_recent": 8.0,
            "roas_change_pct": -20.0,
            "ctr_baseline": 0.013,
            "ctr_recent": 0.012,
            "purchases_per_day_baseline": 1000.0,
            "purchases_per_day_recent": 900.0,
        },
        "suspected_causes": [],
    }

    out = evaluator.evaluate([hyp], summaries={})
    assert len(out) == 1
    h = out[0]
    assert h["status"] == "strong_support"
    assert h["confidence_final"] >= 0.8
    assert len(h["evidence"]) >= 1
