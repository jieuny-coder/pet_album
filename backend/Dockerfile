# Python 3.9 slim 이미지 사용
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# requirements.txt 복사 및 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# pymongo 설치하기 
RUN pip install --no-cache-dir fastapi uvicorn pymongo

#소스 코드 복사
COPY . .

# Uvicorn 서버 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]