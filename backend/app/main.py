from fastapi import FastAPI #FastAPI 가져오기 
from app.routers.main_router import router #라우터 가져오기

app = FastAPI() #FastAPI 애플리케이션 생성


#기존 루트경로
@app.get("/") #루트 URL("/")에 대한 GET 요청 처리 
def read_root():
    return{"message":"반려동물 앨범 프로젝트 서버가 실행중~ "}

# 추가 라우터 연결
# prefix : 라우터에 연결된 경로 앞에 고정적으로 붙는 경로로, API의 경로를 그룹화하거나 다른 경로와 충돌을 방지하기 위해 사용
app.include_router(router, prefix='/api')  # main_router를 FastAPI 앱에 포함시키기 (같은 포트라서 충돌할까봐 prefix 사용해주기)