task_mode = {}

def set_task_mode(device_id: str, value: bool):
    task_mode[device_id] = value

def is_task_mode(device_id: str):
    return task_mode.get(device_id, False)