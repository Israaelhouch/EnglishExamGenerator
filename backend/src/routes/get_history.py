from fastapi import APIRouter, Depends
from backend.src.routes.dependencies import verify_api_key
from backend.src.utils.mongo import get_db

router = APIRouter()

@router.get("/history")
def get_history(_: str = Depends(verify_api_key)):
    db, client = get_db()
    documents = list(db['exam'].find({}, {"_id": 0}))
    client.close()
    return {"history": documents}
