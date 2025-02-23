from openai import AsyncOpenAI
from app.data.config import settings

client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
try:
    client
except Exception as e:
    print(f'Failed to connect to OpenAI (check API key): {e}')


async def gpt_4o(message):
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": str(message)}]
    )
    return response

