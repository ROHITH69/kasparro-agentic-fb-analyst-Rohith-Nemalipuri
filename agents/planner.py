PlannerAgent (src/agents/planner.py)

Input: user query string.
Output: structured plan dict: subtasks like ["identify_time_window", "compute_roas_trends", "find_low_ctr_campaigns"].
Use prompt file prompts/planner.md to map query -> subtasks. Include retry logic if plan is shallow.
