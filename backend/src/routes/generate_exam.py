from fastapi import APIRouter, Query, Depends, HTTPException
from backend.src.routes.dependencies import verify_api_key
from backend.src.utils.mongo import get_db
from backend.src.utils.full_exam_generator import generate_exam 

router = APIRouter()

@router.post("/generate")
def generate(
    chapter: int = Query(..., description="Choose a chapter:\n 1- Education matters\n 2- Life issues\n 3- Creative/inventive minds\n 4- Art shows and holidaying"),
    _: str = Depends(verify_api_key)
):
    if chapter not in [1, 2, 3, 4]:
        raise HTTPException(status_code=400, detail="Chapter not found! Try again")

    chapter, result = generate_exam(chapter)

    db, client = get_db()
    document = {"Chapter": chapter, "Exam": result}
    db['exam'].insert_one(document)
    client.close()

    return {
        "Chapter": chapter,
        "Generated exam": result
    }
