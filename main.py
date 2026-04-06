from fastapi import FastAPI, UploadFile, File
import whisper
import os

app = FastAPI()
model = whisper.load_model("base")

@app.post("/transcribir")
async def transcribir(file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(await file.read())

    result = model.transcribe(temp_path, language="es")
    os.remove(temp_path)

    return {"text": result["text"]}
