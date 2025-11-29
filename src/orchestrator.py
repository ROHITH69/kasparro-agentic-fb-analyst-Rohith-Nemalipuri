from pathlib import Path
import json
from typing import Any, Dict

import pandas as pd

from .agents.planner import PlannerAgent
from .agents.data_agent import DataAgent
from .agents.insight_agent import InsightAgent
from .agents.evaluator import EvaluatorAgent
from .agents.creative_generator import CreativeGeneratorAgent
from .utils.logging_utils import log_event
from .utils.io import load_config, load_data

import uuid
run_id = str(uuid.uuid4())

def run_query(user_query: str) -> Dict[str, Any]:
    config = load_config()
    df: pd.DataFrame = load_data(config)

    log_event("start", {"run_id": run_id, "user_query": user_query})

    # Planner
    planner = PlannerAgent(config=config)
    plan = planner.plan(user_query=user_query, df_columns=list(df.columns))
    log_event("planner", {"plan": plan})

    # Data Agent
    data_agent = DataAgent(config=config)
    summaries = data_agent.summarize(df=df, plan=plan)
    log_event("data_agent", {"summaries_keys": list(summaries.keys())})

    # Insight Agent
    insight_agent = InsightAgent(config=config)
    raw_hypotheses = insight_agent.generate(plan=plan, summaries=summaries)
    log_event("insight_agent", {"num_hypotheses": len(raw_hypotheses)})

    # Evaluator
    evaluator = EvaluatorAgent(config=config)
    validated_insights = evaluator.evaluate(
        hypotheses=raw_hypotheses, summaries=summaries
    )
    log_event("evaluator", {"num_validated": len(validated_insights)})

    # Creative Generator
    creative_agent = CreativeGeneratorAgent(config=config)
    creatives = creative_agent.generate(
        df=df, validated_insights=validated_insights, summaries=summaries
    )
    log_event("creative_generator", {"num_creatives": len(creatives)})

    # Write outputs
   output_dir = Path(f"reports/{run_id}")
output_dir.mkdir(parents=True, exist_ok=True)

insights_path = output_dir / "insights.json"
creatives_path = output_dir / "creatives.json"
report_path = output_dir / "report.md"

    with open(insights_path, "w") as f:
        json.dump(validated_insights, f, indent=2)

    with open(creatives_path, "w") as f:
        json.dump(creatives, f, indent=2)

    # Build a simple report.md using the insights
    report_md = _build_report_md(user_query, validated_insights, summaries)
    with open(report_path, "w") as f:
        f.write(report_md)

    log_event(
        "done",
        {
            "insights_path": str(insights_path),
            "creatives_path": str(creatives_path),
            "report_path": str(report_path),
        },
    )

    return {
        "insights": validated_insights,
        "creatives": creatives,
        "summaries": summaries,
    }


def _build_report_md(
    user_query: str, insights: list[dict], summaries: dict
) -> str:
    overall = summaries["overall"]
    baseline = overall["baseline"]
    recent = overall["recent"]

    def pct_change(new: float, old: float) -> float:
        if old == 0:
            return 0.0
        return (new - old) / old * 100.0

    roas_delta = pct_change(recent["roas"], baseline["roas"])
    ctr_delta = pct_change(recent["ctr"], baseline["ctr"])
    purch_delta = pct_change(
        recent["purchases_per_day"], baseline["purchases_per_day"]
    )

    lines = []
    lines.append(f"# Facebook Performance Diagnosis\n")
    lines.append(f"**Query:** {user_query}\n")
    lines.append("## 1. Executive Summary\n")
    lines.append(
        f"- ROAS dropped from **{baseline['roas']:.2f}** to "
        f"**{recent['roas']:.2f}** (~{roas_delta:.1f}% change).\n"
    )
    lines.append(
        f"- CTR shifted from **{baseline['ctr']*100:.2f}%** to "
        f"**{recent['ctr']*100:.2f}%** (~{ctr_delta:.1f}% change).\n"
    )
    lines.append(
        f"- Purchases per day changed from **{baseline['purchases_per_day']:.0f}** "
        f"to **{recent['purchases_per_day']:.0f}** (~{purch_delta:.1f}% change).\n"
    )

    lines.append("\n## 2. Key Insights\n")
    for hyp in insights:
        lines.append(f"### {hyp['id']}\n")
        lines.append(f"- **Summary:** {hyp['summary']}\n")
        lines.append(f"- **Dimension:** `{hyp['dimension']}`\n")
        lines.append(f"- **Status:** `{hyp['status']}`\n")
        lines.append(
            f"- **Confidence:** {hyp['confidence_final']:.2f} | "
            f"**Impact:** {hyp['impact']}\n"
        )
        if hyp.get("evidence"):
            lines.append("- **Evidence:**")
            for e in hyp["evidence"]:
                lines.append(f"  - {e}")
        if hyp.get("suspected_causes"):
            lines.append("- **Suspected causes:**")
            for c in hyp["suspected_causes"]:
                lines.append(f"  - {c}")
        lines.append("")

    lines.append("## 3. Recommended Next Steps\n")
    lines.append("- Pause or refactor the worst low-CTR clusters.")
    lines.append("- Protect and refresh high-ROAS retargeting audiences.")
    lines.append("- Rebuild video creatives with stronger hooks and product clarity.")
    lines.append("- Re-run this agentic analysis weekly to track changes.\n")

    return "\n".join(lines)
