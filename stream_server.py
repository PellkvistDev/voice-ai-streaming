import asyncio
import websockets
from gpt_stream import stream_chat_response
from eleven import stream_tts_audio

async def handler(websocket, path):
    print("New Twilio stream connected.")
    prompt = "Hej! Har du en minut?"

    try:
        async for word in stream_chat_response(prompt):
            async for audio_chunk in stream_tts_audio(word):
                await websocket.send(audio_chunk)
    except Exception as e:
        print("Error:", e)

start_server = websockets.serve(handler, "0.0.0.0", 10001)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
