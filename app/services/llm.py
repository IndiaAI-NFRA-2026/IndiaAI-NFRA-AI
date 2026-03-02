from app.core.config import settings
# Call OpenRouter directly
from openai import OpenAI

client = OpenAI(
    api_key=settings.OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)

def call_llm(final_prompt: str) -> str:
    response = client.chat.completions.create(
        model="qwen/qwen2.5-vl-32b-instruct",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": final_prompt}
                ]
            }
        ],
        temperature=0.0,
        max_tokens=2048,
    )

    raw_output = response.choices[0].message.content.strip()
    return raw_output