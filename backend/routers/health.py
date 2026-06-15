from fastapi import APIRouter

router = APIRouter(
    tags=["Health"]
)


@router.get("/")
def health_check():
    return {
        "status": "running",
        "service": "AI Customer Support SaaS"
    }