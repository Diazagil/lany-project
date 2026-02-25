from groq import Groq
from app.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

async def speech_to_text(audio_file):
    transcript = client.audio.transcriptions.create(
        model="whisper-large-v3",
        file=(audio_file.filename, audio_file.file, audio_file.content_type)
    )
    print(transcript.text)
    return transcript.text