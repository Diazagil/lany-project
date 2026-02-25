from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import Response
from app.services.stt import speech_to_text
from app.services.llm import generate_response
from app.services.tts import text_to_speech
from app.memory import get_memory, append_message

app = FastAPI()

@app.post("/process")
async def process_audio(
    device_id: str = Form(...),
    file: UploadFile = File(...)
):
    # 1️⃣ STT
    user_text = await speech_to_text(file)

    # 2️⃣ Memory
    append_message(device_id, "user", user_text)
    messages = get_memory(device_id)

    # 3️⃣ LLM
    ai_text = await generate_response(messages)
    append_message(device_id, "assistant", ai_text)

    # 4️⃣ TTS
    audio_bytes = await text_to_speech(ai_text)

    return Response(content=audio_bytes, media_type="audio/mpeg")