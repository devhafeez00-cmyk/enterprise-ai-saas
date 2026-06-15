from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_response(message: str):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """
                You are a professional
                customer support assistant.

                Answer clearly,
                professionally and helpfully.
                """
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return response.choices[0].message.content