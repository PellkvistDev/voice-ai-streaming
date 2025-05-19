from elevenlabs import stream, Voice, VoiceSettings, set_api_key
import os

set_api_key(os.getenv("ELEVEN_API_KEY"))

swedish_voice = Voice(
    voice_id="your-swedish-voice-id",  # e.g., premade or cloned
    settings=VoiceSettings(stability=0.5, similarity_boost=0.8)
)

def stream_tts_audio(text):
    yield from stream(
        text=text,
        voice=swedish_voice,
        model="eleven_monolingual_v1"
    )
