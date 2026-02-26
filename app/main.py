from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import Response
from app.services.stt import speech_to_text
from app.services.llm import generate_response
from app.services.tts import text_to_speech
from app.memory import get_memory, append_message
from app.database import engine, Base, SessionLocal
from app.models.task import Task
from app.routes.voice import set_task_mode, is_task_mode
from app.utils.static_audio import get_static_audio
import re

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/process")
async def process_audio(
    device_id: str = Form(...),
    file: UploadFile = File(...)
):
    # 1️⃣ STT
    # print("masukk mas")
    user_text = await speech_to_text(file)
    # print("user_text", user_text)
    lower_text = user_text.lower()
    # print("lower_test", lower_text)
    # print("is_task_mode", is_task_mode(device_id))
    
    # set_task_mode(device_id, False)
    if "add task" in lower_text:
        set_task_mode(device_id, True)
        return get_static_audio("ask_task.wav")
    
    if is_task_mode(device_id):
        print(is_task_mode(device_id))

        db = SessionLocal()

        new_task = Task(
            device_id=device_id,
            title=user_text
        )

        db.add(new_task)
        db.commit()
        db.close()

        set_task_mode(device_id, False)

        return get_static_audio("task_added.wav")

    if "view task" in lower_text:
        db = SessionLocal()
        
        tasks = db.query(Task).all()
        
        db.close()

        if not tasks:
            return get_static_audio("no_task.wav")

        # Buat teks respons
        response_text = f"You have {len(tasks)} tasks. "
        
        for i, task in enumerate(tasks, start=1):
            response_text += f"{i}. {task.title}. "

        audio_bytes = await text_to_speech(response_text)

        return Response(content=audio_bytes, media_type="audio/mpeg")

    if "complete task" in lower_text:
        match = re.search(r"complete task (\d+)", lower_text)
        
        if not match:
            return get_static_audio("invalid_task_number.wav")

        task_number = int(match.group(1))

        db = SessionLocal()

        tasks = db.query(Task).filter().all()

        if task_number < 1 or task_number > len(tasks):
            db.close()
            return get_static_audio("invalid_task_number.wav")

        task_to_delete = tasks[task_number - 1]

        db.delete(task_to_delete)
        db.commit()
        db.close()

        return get_static_audio("task_completed.wav")

    # 2️⃣ Memory
    append_message(device_id, "user", user_text)
    messages = get_memory(device_id)

    # 3️⃣ LLM
    ai_text = await generate_response(messages)
    append_message(device_id, "assistant", ai_text)

    # 4️⃣ TTS
    audio_bytes = await text_to_speech(ai_text)

    return Response(content=audio_bytes, media_type="audio/mpeg")