from elevenlabs import stream, Voice, VoiceSettings, Elevenlabs
import os

elevenlabs_client = ElevenLabs(
    api_key="sk_2298d3907994dc6225854c594ed8a9ccd07aa1dfffcad031"
)

swedish_voice = Voice(
    voice_id="your-swedish-voice-id",  # e.g., premade or cloned
    settings=VoiceSettings(stability=0.5, similarity_boost=0.8)
)

def stream_tts_audio(text):
    yield from stream(
        text=text,
        voice=swedish_voice,
        model="eleven_flash_v2"
    )
