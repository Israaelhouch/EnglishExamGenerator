from fastapi import APIRouter, UploadFile, File, HTTPException
import whisper
import shutil
import os

router = APIRouter()

model = whisper.load_model("medium")

@router.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    try:
        file_path = f"temp_{file.filename}"
        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        result = model.transcribe(file_path)
        
        os.remove(file_path)
        
        return {"text": result["text"]}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")
