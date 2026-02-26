from fastapi.responses import Response

def get_static_audio(filename: str):
    with open(f"app/static/audio/{filename}", "rb") as f:
        return Response(
            content=f.read(),
            media_type="audio/mpeg"
        )