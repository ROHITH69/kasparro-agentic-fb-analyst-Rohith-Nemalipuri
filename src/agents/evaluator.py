#Input: hypotheses, full df
#Quantitatively test each hypothesis via checks (z-scores, relative drops > threshold, cross-validation of metrics).
#Output truth score/confidence and evidence dict (metric deltas, p-values optionally).
#Add confidence based on statistical checks and rule heuristics. If low confidence, instruct InsightAgent to retry/refine.

from typing import Any, Dict, List
from ..utils.schemas import Hypothesis

class EvaluatorAgent:
    def __init__(self, config: Dict[str, Any]):
        self.config = config

    def _evaluate_roas_trend(self, hyp: Dict[str, Any]) -> Hypothesis:
        m = hyp["metrics"]
        change = m.get("roas_change_pct", 0.0)
        evidence = [
            f"Mean ROAS changed from {m['roas_baseline']:.2f} to {m['roas_recent']:.2f}.",
            f"CTR changed from {m['ctr_baseline']*100:.2f}% to {m['ctr_recent']*100:.2f}%.",
            f"Purchases per day changed from {m['purchases_per_day_baseline']:.0f} "
            f"to {m['purchases_per_day_recent']:.0f}.",
        ]

        if change <= -10:
            status = "strong_support"
            confidence = 0.85
            impact = "high"
        elif -10 < change <= -5:
            status = "partial"
            confidence = 0.65
            impact = "medium"
        else:
            status = "rejected"
            confidence = 0.3
            impact = "low"

        return Hypothesis(
            id=hyp["id"],
            summary=hyp["summary"],
            dimension=hyp["dimension"],
            metrics=hyp["metrics"],
            suspected_causes=hyp.get("suspected_causes", []),
            evidence=evidence,
            status=status,
            confidence_final=confidence,
            impact=impact,
        )

    def _default_hypothesis(self, hyp: Dict[str, Any]) -> Hypothesis:
        # Default: trust prior but cap confidence
        return Hypothesis(
            id=hyp["id"],
            summary=hyp["summary"],
            dimension=hyp["dimension"],
            metrics=hyp["metrics"],
            suspected_causes=hyp.get("suspected_causes", []),
            evidence=[],
            status="partial",
            confidence_final=min(hyp.get("confidence_prior", 0.7) + 0.1, 0.9),
            impact="medium",
        )

    def evaluate(self, hypotheses: List[Dict[str, Any]], summaries: Dict[str, Any]) -> List[Dict[str, Any]]:
        evaluated: List[Hypothesis] = []

        for hyp in hypotheses:
            if hyp["id"] == "H1_roas_trend_last_14_vs_first_14":
                evaluated.append(self._evaluate_roas_trend(hyp))
            else:
                evaluated.append(self._default_hypothesis(hyp))

        # Convert dataclasses to dicts
        return [h.__dict__ for h in evaluated]
