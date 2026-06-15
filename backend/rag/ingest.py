from pypdf import PdfReader

from rag.chroma_client import (
    collection
)

from rag.embeddings import (
    create_embedding
)


def ingest_pdf(file_path):

    pdf = PdfReader(file_path)

    text = ""

    for page in pdf.pages:
        text += page.extract_text()

    chunks = [
        text[i:i + 1000]
        for i in range(
            0,
            len(text),
            1000
        )
    ]

    for index, chunk in enumerate(chunks):

        embedding = create_embedding(
            chunk
        )

        collection.add(
            ids=[str(index)],
            embeddings=[embedding],
            documents=[chunk]
        )