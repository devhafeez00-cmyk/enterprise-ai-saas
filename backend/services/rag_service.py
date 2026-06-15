from openai import OpenAI

import os

from rag.retrieval import (
    retrieve_context
)

client = OpenAI(
    api_key=os.getenv(
        "OPENAI_API_KEY"
    )
)


def rag_chat(question):

    context = retrieve_context(
        question
    )

    prompt = f"""
    Use only the context below.

    Context:
    {context}

    Question:
    {question}
    """

    response = (
        client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
    )

    return (
        response
        .choices[0]
        .message.content
    )