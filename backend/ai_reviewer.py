from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def review_code(patch):   # FIX: parameter name corrected

    prompt = f"""
You are a senior software engineer reviewing a GitHub pull request.

Analyze this code diff and provide:

1. Bugs
2. Security issues
3. Performance issues
4. Code smells

Rules:
- Keep response under 150 words
- Use bullet points
- Mention severity: Low/Medium/High
- Be concise
- Do not explain obvious things
- Only report real issues

Code diff:
{patch}
"""

    try:
        completion = client.chat.completions.create(
            model="deepseek/deepseek-chat",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"AI Review Error: {str(e)}"