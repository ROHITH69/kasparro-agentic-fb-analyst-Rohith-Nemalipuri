# src/orchestrator.py
import os
import json
from agents.planner import PlannerAgent
from agents.data_agent import DataAgent
from agents.insight_agent import InsightAgent
from agents.evaluator import EvaluatorAgent
from agents.creative_generator import CreativeGenerator
from utils.io import write_json, ensure_dir
from datetime import datetime

class Orchestrator:
    def __init__(self, cfg):
        self.cfg = cfg
        self.data_agent = DataAgent(cfg)
        self.planner = PlannerAgent(cfg)
        self.insight_agent = InsightAgent(cfg)
        self.evaluator = EvaluatorAgent(cfg)
        self.creative_gen = CreativeGenerator(cfg)
        ensure_dir(cfg["reports_dir"])
        ensure_dir(cfg["logs_dir"])

    def run(self, query):
        trace = {"query": query, "started_at": datetime.utcnow().isoformat()}
        # 1. Planner: decompose
        plan = self.planner.decompose(query)
        trace["plan"] = plan

        # 2. Data agent: load & summarize (only pass summaries forward)
        data_summary = self.data_agent.load_and_summarize()
        trace["data_summary"] = data_summary

        # 3. Insight agent: hypotheses
        hypotheses = self.insight_agent.generate(data_summary, plan)
        trace["hypotheses"] = hypotheses

        # 4. Evaluator: validate
        evaluated = self.evaluator.validate(hypotheses, self.data_agent.dataframe)
        trace["evaluated"] = evaluated

        # 5. Creative generator: generate creatives for low-CTR campaigns
        creatives = self.creative_gen.generate(evaluated, data_summary)
        trace["creatives"] = creatives

        # 6. Write outputs
        ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
        write_json(evaluated, os.path.join(self.cfg["reports_dir"], "insights.json"))
        write_json(creatives, os.path.join(self.cfg["reports_dir"], "creatives.json"))
        # Basic report
        report_md = self._build_report(evaluated, creatives, data_summary, plan)
        with open(os.path.join(self.cfg["reports_dir"], "report.md"), "w") as f:
            f.write(report_md)

        # logs
        write_json(trace, os.path.join(self.cfg["logs_dir"], f"run_trace_{ts}.json"))
        print("Run complete. Reports written to", self.cfg["reports_dir"])

    def _build_report(self, evaluated, creatives, data_summary, plan):
        # produce short markdown report; Insight -> Evidence -> Recommendation
        lines = ["# Kasparro Agentic FB Performance Analyst Report", ""]
        lines.append("## Executive Summary")
        lines.append(f"- Query: {plan.get('query', 'N/A')}")
        lines.append("")
        lines.append("## Top Hypotheses")
        for h in evaluated.get("hypotheses", []):
            lines.append(f"### {h['id']}: {h['title']}")
            lines.append(f"- Confidence: {h['confidence']:.2f}")
            lines.append(f"- Evidence summary: {h['evidence_summary']}")
            lines.append("")
        lines.append("## Creative Recommendations")
        for c in creatives.get("recommendations", []):
            lines.append(f"- Campaign: {c['campaign_name']}")
            lines.append(f"  - Headline: {c['headline']}")
            lines.append(f"  - Body: {c['body']}")
            lines.append(f"  - CTA: {c['cta']}")
            lines.append("")
        return "\n".join(lines)

