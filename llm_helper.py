# llm_helper.py
from openai import OpenAI
import os

# Initialize OpenAI client using environment variable for API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_llm_response(prompt: str) -> str:
    """
    Send a prompt to the OpenAI LLM and return the response text.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


