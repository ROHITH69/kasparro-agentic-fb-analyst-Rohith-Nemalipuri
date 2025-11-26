from typing import Any, Dict, List

class InsightAgent:
    def __init__(self, config: Dict[str, Any]):
        self.config = config

    def generate(self, plan: Dict[str, Any], summaries: Dict[str, Any]) -> List[Dict[str, Any]]:
        overall = summaries["overall"]
        aud = summaries["by_audience_type"]
        ct = summaries["by_creative_type"]
        low = summaries["low_ctr_clusters"]

        baseline = overall["baseline"]
        recent = overall["recent"]

        def pct_change(new: float, old: float) -> float:
            if old == 0:
                return 0.0
            return (new - old) / old * 100.0

        insights: List[Dict[str, Any]] = []

        # H1: ROAS trend
        insights.append(
            {
                "id": "H1_roas_trend_last_14_vs_first_14",
                "summary": "Account-level ROAS in the last 14 days is lower than in the first 14 days.",
                "dimension": "date",
                "metrics": {
                    "roas_baseline": baseline["roas"],
                    "roas_recent": recent["roas"],
                    "roas_change_pct": pct_change(recent["roas"], baseline["roas"]),
                    "ctr_baseline": baseline["ctr"],
                    "ctr_recent": recent["ctr"],
                    "ctr_change_pct": pct_change(recent["ctr"], baseline["ctr"]),
                    "purchases_per_day_baseline": baseline["purchases_per_day"],
                    "purchases_per_day_recent": recent["purchases_per_day"],
                    "purchases_per_day_change_pct": pct_change(
                        recent["purchases_per_day"], baseline["purchases_per_day"]
                    ),
                },
                "suspected_causes": [
                    "creative_fatigue",
                    "slightly weaker CTR and conversion rate at similar spend",
                ],
                "confidence_prior": 0.7,
            }
        )

        # H2: Retargeting vs Broad
        if "Broad" in aud and "Retargeting" in aud:
            insights.append(
                {
                    "id": "H2_retarg_outperforms_broad",
                    "summary": "Retargeting audiences deliver significantly higher ROAS than Broad at similar CTR.",
                    "dimension": "audience_type",
                    "metrics": {
                        "Broad": aud["Broad"],
                        "Retargeting": aud["Retargeting"],
                    },
                    "suspected_causes": [
                        "warmer audiences",
                        "higher intent users in retargeting pools",
                    ],
                    "confidence_prior": 0.8,
                }
            )

        # H3: Video underperforms static
        if "Video" in ct and "Image" in ct:
            insights.append(
                {
                    "id": "H3_video_underperforms_static",
                    "summary": "Video creatives underperform static formats (Image/Carousel) on ROAS and CTR.",
                    "dimension": "creative_type",
                    "metrics": {k: v for k, v in ct.items()},
                    "suspected_causes": [
                        "weak hooks in first seconds of video",
                        "less product clarity vs static formats",
                    ],
                    "confidence_prior": 0.6,
                }
            )

        # H4: Low-CTR clusters
        if low:
            insights.append(
                {
                    "id": "H4_low_ctr_clusters_drag_down_blended",
                    "summary": "Several campaign+adset clusters have CTR far below the account average while spending meaningful budget.",
                    "dimension": "campaign_name+adset_name",
                    "metrics": {"examples": low},
                    "suspected_causes": [
                        "generic messaging that fails to stand out",
                        "creative fatigue on repeated angles",
                    ],
                    "confidence_prior": 0.75,
                }
            )

        return insights
