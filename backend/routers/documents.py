from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

import os

from rag.ingest import (
    ingest_pdf
)

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):

    path = f"uploads/{file.filename}"

    with open(path, "wb") as buffer:
        buffer.write(
            await file.read()
        )

    ingest_pdf(path)

    return {
        "message":
        "Document uploaded successfully"
    }