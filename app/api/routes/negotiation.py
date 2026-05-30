from fastapi import (
    APIRouter
)

from app.services.negotiation_service import (
    run_negotiation,
    continue_negotiation
)

router = APIRouter()


@router.post("/negotiate")
def negotiate(
    payload: dict
):

    query = payload.get(
        "user_query"
    )

    result = run_negotiation(
        query
    )

    return result


@router.post("/clarify")
def clarify(
    payload: dict
):

    result = continue_negotiation(
        user_query=
            payload.get(
                "user_query"
            ),

        clarification=
            payload.get(
                "clarification"
            )
    )

    return result