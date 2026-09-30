from typing import TypedDict

from langgraph.graph import StateGraph, START, END
from pathlib import Path
from agent.planner import planner_agent
from agent.architect import architect_agent
from agent.coder import coder_agent
from agent.project_analyzer import project_analyzer

class AgentState(TypedDict):
    user_request: str
    plan: str
    architecture: str
    code_plan: str
    project_content : str
    project_analysis:str


def planner_node(state: AgentState):
    plan = planner_agent(state["user_request"])

    return {
        "plan": plan
    }


def architect_node(state: AgentState):
    architecture = architect_agent(state["plan"],state["project_analysis"])

    return {
        "architecture": architecture
    }

def coder_node(state: AgentState):
    code_plan = coder_agent(
        state["plan"],
        state["architecture"],
        state["project_analysis"]
    )

    return {
        "code_plan": code_plan
    }

def project_analyzer_node(state: AgentState):
    analysis = project_analyzer(state["project_content"])
    return {"project_analysis": analysis}



graph = StateGraph(AgentState)

graph.add_node("project_analyzer", project_analyzer_node)
graph.add_node("planner", planner_node)
graph.add_node("architect", architect_node)
graph.add_node("coder", coder_node)

graph.add_edge(START, "project_analyzer")
graph.add_edge("project_analyzer", "planner")
graph.add_edge("planner", "architect")
graph.add_edge("architect", "coder")
graph.add_edge("coder", END)

app = graph.compile()