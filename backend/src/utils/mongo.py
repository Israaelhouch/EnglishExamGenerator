from pymongo import MongoClient
from backend.src.routes.dependencies import MONGO_URI

def get_db():
    client = MongoClient(MONGO_URI)
    return client['EnglishExams'], client