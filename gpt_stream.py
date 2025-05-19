import openai
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Eller ersätt med din nyckel direkt

async def stream_chat_response(prompt):
    messages = [{"role": "system", "content": "Du ska sälja en höbal för 200000kr."},
                {"role": "user", "content": prompt}]
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        stream=True
    )
    
    async for chunk in response:
        delta = chunk["choices"][0]["delta"]
        if "content" in delta:
            yield delta["content"]
