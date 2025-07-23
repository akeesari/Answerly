import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def query_llm(prompt: str) -> str:
    print("Using ChatCompletion API")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=500,
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"LLM error: {str(e)}"
