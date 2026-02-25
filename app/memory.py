conversation_memory = {}

def get_memory(device_id: str):
    if device_id not in conversation_memory:
        conversation_memory[device_id] = [
            {
                "role": "system",
                "content": "You are Lany, a friendly voice assistant. Always respond in english"
            }
        ]
    return conversation_memory[device_id]

def append_message(device_id: str, role: str, content: str):
    memory = get_memory(device_id)
    memory.append({"role": role, "content": content})

    # Batasi memory 10 pesan terakhir
    if len(memory) > 20:
        conversation_memory[device_id] = memory[-20:]