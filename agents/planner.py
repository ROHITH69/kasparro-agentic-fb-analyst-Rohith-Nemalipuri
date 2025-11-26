PlannerAgent (src/agents/planner.py)

Input: user query string.
Output: structured plan dict: subtasks like ["identify_time_window", "compute_roas_trends", "find_low_ctr_campaigns"].
Use prompt file prompts/planner.md to map query -> subtasks. Include retry logic if plan is shallow.

from typing import Any, Dict, List

class PlannerAgent:
    """
    Extremely simple planner.
    In a real system this would call an LLM with prompts/planner.md
    to decide the plan. Here we return a fixed but reasonable plan
    based on the user query.
    """
    def __init__(self, config: Dict[str, Any]):
        self.config = config

    def plan(self, user_query: str, df_columns: List[str]) -> Dict[str, Any]:
        steps = [
            {
                "id": "step_1_data_summary",
                "agent": "data_agent",
                "description": "Summarize account, audience_type, creative_type, low_ctr clusters.",
                "inputs": {},
            },
            {
                "id": "step_2_generate_hypotheses",
                "agent": "insight_agent",
                "description": "Generate hypotheses explaining performance patterns.",
                "inputs": {"from": "step_1_data_summary"},
            },
            {
                "id": "step_3_evaluate_hypotheses",
                "agent": "evaluator",
                "description": "Numerically validate each hypothesis.",
                "inputs": {"from": "step_2_generate_hypotheses"},
            },
            {
                "id": "step_4_generate_creatives",
                "agent": "creative_generator",
                "description": "Generate creative ideas for low-CTR clusters.",
                "inputs": {"from": "step_3_evaluate_hypotheses"},
            },
        ]
        return {"user_query": user_query, "steps": steps, "columns": df_columns}
