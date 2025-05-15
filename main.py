import os
from fastapi import FastAPI, Query, Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from backend.src.routes.exam_generator import generate_exam
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()

MONGO_URI = os.getenv("MONGODB_URL")
API_KEY = os.getenv("API_KEY")

app = FastAPI()
api_key_header = APIKeyHeader(name="API-Key")

def verify_api_key(key: str = Security(api_key_header)):
    if key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")


@app.post("/generate")
def generate(
    chapter: int = Query(..., description="Choose a chapter:\n 1- Education matters\n 2- Life issues\n 3- Creative/inventive minds\n 4- Art shows and holidaying"),
    api_key: str = Depends(verify_api_key)):
    if chapter not in [1, 2, 3, 4]:
        raise HTTPException(status_code=400, detail="Chapter not found! Try again")

    chapter, result = generate_exam(chapter)

    
    client = MongoClient(MONGO_URI)
    db = client['EnglishExams']
    collection = db['exam']
    document = {"Chapter": chapter, "Exam": result}
    collection.insert_one(document)
    client.close()

    return {
        "Chapter": chapter,
        "Generated exam": result
    }


@app.get("/history")
def get_history(api_key: str = Depends(verify_api_key)):
    client = MongoClient(MONGO_URI)
    db = client['EnglishExams']
    collection = db['exam']
    documents = list(collection.find({}, {"_id": 0}))
    client.close()

    return {"history": documents}
