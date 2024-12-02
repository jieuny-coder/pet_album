# Node.js 16버전 이미지를 기반으로 사용
FROM node:16

# 작업 디렉토리 설정 (컨테이너 내부에서 /app 디렉토리를 작업 디렉토리로 지정하기)
WORKDIR /app

# package.json 파일 복사 및 의존성 설치
# (package.json과 package-lock.json 파일을 컨테이너 내부로 복사하기)
# (npm install 명령어로 Vue.js 의존성 설치)
COPY package*.json ./ 
RUN npm install

# 소스 코드 복사
#(프로젝트의 모든 소스 파일을 컨테이너 내부의 /app 디렉토리로 복사하기)
COPY . .

# Vue.js 개발 서버 실행
CMD ["npm", "run","dev"]