from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database import get_db

from services.openai_service import (
    generate_response
)

from schemas.chat import (
    ChatRequest
)

from models.conversation import (
    Conversation
)

from services.rag_service import (
    rag_chat
)

router = APIRouter(
    prefix="/chat",
    tags=["AI Chat"]
)


@router.post("/")
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):

    ai_reply = rag_chat(
        request.message
    )

    conversation = Conversation(
        user_id=1,
        user_message=request.message,
        ai_response=ai_reply
    )

    db.add(conversation)

    db.commit()

    return {
        "response": ai_reply
    }

@router.get("/history")
def get_history(
    db: Session = Depends(get_db)
):

    conversations = db.query(
        Conversation
    ).all()

    return conversations