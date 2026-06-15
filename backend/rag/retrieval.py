from rag.chroma_client import (
    collection
)

from rag.embeddings import (
    create_embedding
)


def retrieve_context(question):

    embedding = create_embedding(
        question
    )

    result = collection.query(
        query_embeddings=[embedding],
        n_results=3
    )

    docs = result["documents"][0]

    return "\n".join(docs)