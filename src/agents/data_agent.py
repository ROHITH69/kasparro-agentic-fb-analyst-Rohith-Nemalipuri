from typing import Any, Dict

import pandas as pd

class DataAgent:
    def __init__(self, config: Dict[str, Any]):
        self.config = config

    def summarize(self, df: pd.DataFrame, plan: Dict[str, Any]) -> Dict[str, Any]:
        date_col = self.config["data"].get("date_column", "date")
        df = df.sort_values(date_col)

        unique_dates = df[date_col].sort_values().unique()
        baseline_days = self.config["windows"]["baseline_days"]
        comparison_days = self.config["windows"]["comparison_days"]

        baseline_dates = unique_dates[:baseline_days]
        recent_dates = unique_dates[-comparison_days:]

        baseline = df[df[date_col].isin(baseline_dates)]
        recent = df[df[date_col].isin(recent_dates)]

        def agg_metrics(sub: pd.DataFrame) -> Dict[str, float]:
            spend = sub["spend"].sum()
            revenue = sub["revenue"].sum()
            impressions = sub["impressions"].sum()
            clicks = sub["clicks"].sum()
            purchases = sub["purchases"].sum()
            days = sub[date_col].nunique() or 1
            return {
                "roas": float(revenue / spend) if spend > 0 else 0.0,
                "ctr": float(clicks / impressions) if impressions > 0 else 0.0,
                "purchases_per_day": float(purchases / days),
            }

        overall = {
            "baseline": {
                "start_date": str(baseline[date_col].min().date()),
                "end_date": str(baseline[date_col].max().date()),
                **agg_metrics(baseline),
            },
            "recent": {
                "start_date": str(recent[date_col].min().date()),
                "end_date": str(recent[date_col].max().date()),
                **agg_metrics(recent),
            },
        }

        def group_metrics(group: pd.core.groupby.DataFrameGroupBy) -> Dict[str, Any]:
            out: Dict[str, Any] = {}
            for key, sub in group:
                spend = sub["spend"].sum()
                revenue = sub["revenue"].sum()
                impressions = sub["impressions"].sum()
                clicks = sub["clicks"].sum()
                purchases = sub["purchases"].sum()
                out[str(key)] = {
                    "spend": float(spend),
                    "revenue": float(revenue),
                    "impressions": int(impressions),
                    "clicks": float(clicks),
                    "purchases": int(purchases),
                    "roas": float(revenue / spend) if spend > 0 else 0.0,
                    "ctr": float(clicks / impressions) if impressions > 0 else 0.0,
                }
            return out

        by_audience_type = group_metrics(df.groupby("audience_type"))
        by_creative_type = group_metrics(df.groupby("creative_type"))

        # Low-CTR clusters
        thresholds = self.config["thresholds"]
        min_impr = thresholds["min_impressions"]
        min_spend = thresholds["min_spend"]

        grouped = (
            df.groupby(["campaign_name", "adset_name"])
            .agg(
                spend=("spend", "sum"),
                revenue=("revenue", "sum"),
                impressions=("impressions", "sum"),
                clicks=("clicks", "sum"),
                purchases=("purchases", "sum"),
            )
            .reset_index()
        )

        grouped["ctr"] = grouped["clicks"] / grouped["impressions"]
        grouped["roas"] = grouped["revenue"] / grouped["spend"]

        low_ctr_clusters = (
            grouped[
                (grouped["impressions"] >= min_impr)
                & (grouped["spend"] >= min_spend)
                & (grouped["ctr"] > 0)
            ]
            .sort_values("ctr")
            .head(10)
        )

        low_clusters_json = [
            {
                "campaign_name": row["campaign_name"],
                "adset_name": row["adset_name"],
                "spend": float(row["spend"]),
                "revenue": float(row["revenue"]),
                "impressions": int(row["impressions"]),
                "clicks": float(row["clicks"]),
                "purchases": int(row["purchases"]),
                "ctr": float(row["ctr"]),
                "roas": float(row["roas"]),
            }
            for _, row in low_ctr_clusters.iterrows()
        ]

        return {
            "overall": overall,
            "by_audience_type": by_audience_type,
            "by_creative_type": by_creative_type,
            "low_ctr_clusters": low_clusters_json,
        }
