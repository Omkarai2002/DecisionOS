from langgraph.graph import StateGraph, END

from app.graph.state import AgentState
from app.graph.nodes import (
    finance_node,
    health_node,
    career_node,
    social_node,
    time_node,
    rebuttal_node,
    orchestrator_node
)


def build_graph():

    builder = StateGraph(AgentState)

    builder.add_node("finance", finance_node)
    builder.add_node("health", health_node)
    builder.add_node("career", career_node)
    builder.add_node("social", social_node)
    builder.add_node("time", time_node)
    builder.add_node("orchestrator", orchestrator_node)
    builder.add_node("rebuttal",rebuttal_node)
    builder.set_entry_point("finance")

    builder.add_edge("finance", "health")
    builder.add_edge("health", "career")
    builder.add_edge("career", "social")
    builder.add_edge("social", "time")
    builder.add_edge("time", "rebuttal")
    builder.add_edge("rebuttal","orchestrator")
    builder.add_edge("orchestrator", END)

    return builder.compile()