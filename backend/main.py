from fastapi import FastAPI

from database import Base
from database import engine

from auth.routes import router as auth_router
from routers.health import router as health_router
from routers.chat import (
    router as chat_router
)

from models.user import User
from models.conversation import Conversation

from routers.documents import (
    router as document_router
)



Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Customer Support SaaS",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(chat_router)
app.include_router(health_router)


@app.get("/ping")
def ping():
    return {
        "message": "pong"
    }

    app.include_router(
    document_router
)