from pymongo import MongoClient

# MongoDB 클라이언트 설정
# MongoDB 컨테이너 이름(mongodb)과 기본 포트(27017)를 사용해 연결
client = MongoClient("mongodb://mongodb:27017")  # Docker Compose의 컨테이너 이름 사용
db = client["pet_album"] # 데이터베이스 이름 설정