from fastapi import APIRouter
from app.models.database import db # MongoDB 연결 가져오기

router = APIRouter()

@router.get("/")
def root():
    return{"message":"Welcome to th Pet Album API!"}

@router.get("/db-test")
def db_test():
    # MongoDB에 샘플데이터 삽입
    db.test_collection.insert_one({"test_key":"test_value"})
    # MongoDB에서 데이터 읽기
    result = db.test_collection.find_one({"test_key":"test_value"})
    return {"result": str(result)}