from fastapi import APIRouter, HTTPException
from transformers import pipeline

router = APIRouter()

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@router.post("/summarize/")
async def summarize_text(text: str):
    try:
        summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
        return {"summary": summary[0]["summary_text"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error summarizing text: {str(e)}")
