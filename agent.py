from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini

from app.security import is_injection, redact_pii


# -------------------------
# 1. SECURITY NODE
# -------------------------
def security_node(query: str) -> str:
    clean = redact_pii(query)

    if is_injection(clean):
        return "Blocked: unsafe or injection-like request detected."

    return clean


# -------------------------
# 2. PLANNER NODE
# -------------------------
def planner_node(query: str) -> str:
    return f"""
Study Plan:
1. Priorities → Extract key topics from: {query}
2. Schedule → Morning (hard topics), Afternoon (practice), Evening (review)
3. Study Techniques → Active recall, Pomodoro, practice exams
4. Motivation Tips → Break tasks into small goals and stay consistent
""".strip()


# -------------------------
# 3. MOTIVATION NODE
# -------------------------
def motivation_node(plan: str) -> str:
    return plan + """

Bonus Motivation:
You are capable of handling this exam week. Stay consistent, not perfect.
"""


# -------------------------
# ORCHESTRATOR TOOL (GRAPH SIMULATION)
# -------------------------
def study_workflow(query: str) -> str:
    safe_input = security_node(query)
    if "Blocked" in safe_input:
        return safe_input

    plan = planner_node(safe_input)
    final = motivation_node(plan)

    return final


# -------------------------
# ROOT AGENT (ADK ENTRYPOINT)
# -------------------------
root_agent = Agent(
    name="study_buddy_ai",
    model=Gemini(model="gemini-flash-latest"),

    instruction="""
You are a workflow-based AI agent.

Always use the study_workflow tool to respond.
Do not generate responses directly.
""",

    tools=[study_workflow],
)


app = App(
    root_agent=root_agent,
    name="app",
)