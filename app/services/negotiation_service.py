from app.graph.workflow import (
    build_graph
)

graph = build_graph()


def run_negotiation(
    user_query: str
):

    initial_state = {
        "user_query": user_query,
        "messages": [],
        "agent_outputs": [],
        "final_decision": {},
        "clarification_question":
            None,
        "user_clarification":
            None,
        "negotiation_round":
            1
    }

    result = graph.invoke(
        initial_state
    )

    return result


def continue_negotiation(
    user_query: str,
    clarification: str
):

    initial_state = {
        "user_query":
            user_query,

        "messages": [],

        "agent_outputs": [],

        "final_decision": {},

        "clarification_question":
            None,

        "user_clarification":
            clarification,

        "negotiation_round":
            2
    }

    result = graph.invoke(
        initial_state
    )

    return result