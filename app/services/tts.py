from groq import Groq
from app.config import GROQ_API_KEY

client = Groq(
    api_key=GROQ_API_KEY
)

async def text_to_speech(text: str):
    speech = client.audio.speech.create(
        model="canopylabs/orpheus-v1-english",
        input=text,
        voice="autumn",
        response_format="wav"
    )
    return speech.read()