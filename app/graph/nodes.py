from app.graph.state import AgentState

from app.agents.career_agent import (
    CareerAgent
)

from app.agents.finance_agent import (
    FinanceAgent
)

from app.agents.health_agent import (
    HealthAgent
)

from app.agents.social_agent import (
    SocialAgent
)

from app.agents.time_agent import (
    TimeAgent
)

from app.agents.clarification_agent import (
    ClarificationAgent
)

from app.schemas.clarification import (
    ClarificationQuestion
)

from app.schemas.rebuttal import (
    RebuttalOutput
)

career_agent = CareerAgent()
finance_agent = FinanceAgent()
health_agent = HealthAgent()
social_agent = SocialAgent()
time_agent = TimeAgent()
clarification_agent= ClarificationAgent()

def finance_node(state):
    print("Finance Agent Running")

    result = finance_agent.run(
        state["user_query"],
        clarification=
            state.get(
                "user_clarification",
                ""
            )
    )

    state["agent_outputs"].append(
        result.model_dump()
    )

    return state


def health_node(state):
    print("Health Agent Running")

    result = health_agent.run(
        state["user_query"],
        clarification=
            state.get(
                "user_clarification",
                ""
            )
    )

    state["agent_outputs"].append(
        result.model_dump()
    )

    return state


def career_node(state):
    print("Career Agent Running")

    result = career_agent.run(
        user_query=
            state["user_query"],

        clarification=
            state.get(
                "user_clarification",
                ""
            )
    )
    state["agent_outputs"].append(
        result.model_dump()
    )

    return state

def social_node(state):
    print("Social Agent Running")

    result = social_agent.run(
        state["user_query"],
        clarification=
            state.get(
                "user_clarification",
                ""
            )
    )

    state["agent_outputs"].append(
        result.model_dump()
    )

    return state


def time_node(state):
    print("Time Agent Running")

    result = time_agent.run(
        state["user_query"],
        clarification=
            state.get(
                "user_clarification",
                ""
            )
    )

    state["agent_outputs"].append(
        result.model_dump()
    )

    return state

def rebuttal_node(state):

    print("Rebuttal Round Running")

    rebuttals = []

    peer_context = "\n\n".join([
        f"""
        Agent:
        {a["agent_name"]}

        Vote:
        {a["vote"]}

        Confidence:
        {a["confidence"]}

        Reasoning:
        {a["reasoning"]}
        """
        for a in state[
            "agent_outputs"
        ]
    ])

    agents = {
        "finance":
            finance_agent,

        "health":
            health_agent,

        "career":
            career_agent,

        "social":
            social_agent,

        "time":
            time_agent
    }

    for output in state[
        "agent_outputs"
    ]:

        agent_name = output[
            "agent_name"
        ]

        agent = agents[
            agent_name
        ]

        result = agent.run(
            user_query=
                state[
                    "user_query"
                ],

            clarification=
                state.get(
                    "user_clarification",
                    ""
                ),

            peer_context=
                peer_context,

            response_model=
                RebuttalOutput
        )

        rebuttals.append(
            result.model_dump()
        )

    state[
        "rebuttals"
    ] = rebuttals

    return state

def orchestrator_node(state):
    print("Orchestrator Running")
    rebuttal_lookup = {
            r["agent_name"]: r
            for r in state.get(
                "rebuttals",
                []
            )
        }
    vote_weights = {
        "accept": 1,
        "neutral": 0,
        "reject": -1
    }

    total_score = 0

    decision_breakdown = []

    for output in state["agent_outputs"]:
        updated_confidence = (
            rebuttal_lookup
            .get(
                output[
                    "agent_name"
                ],
                {}
            )
            .get(
                "updated_confidence",
                output[
                    "confidence"
                ]
            )
        )
        weighted_score = (
            vote_weights[
                output["vote"]
            ]
            * updated_confidence
        )

        total_score += weighted_score

        decision_breakdown.append({
            "agent": output["agent_name"],
            "vote": output["vote"],
            "confidence": output["confidence"],
            "weighted_score": weighted_score
        })

    if total_score > 0.25:
        final_decision = "accept"

    elif total_score < -0.25:
        final_decision = "reject"

    else:

        current_round = state.get(
            "negotiation_round",
            1
        )

        if current_round == 1:

            final_decision = "deadlock"

            agent_summary = str(
                state["agent_outputs"]
            )

            result = (
                clarification_agent.run(
                    user_query=
                        agent_summary,
                    response_model=
                        ClarificationQuestion
                )
            )

            state[
                "clarification_question"
            ] = result.question

        else:

            final_decision = (
                "neutral"
            )

    state["final_decision"] = {
        "decision": final_decision,
        "total_score": round(
            total_score,
            2
        ),
        "decision_breakdown":
            decision_breakdown
    }

    return state