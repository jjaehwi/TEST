# 모바일 청첩장 프로젝트

React 기반 반응형 모바일 청첩장입니다. 계좌번호 복사, 동영상 재생, 댓글 기능이 포함되어 있습니다.

## 기능

- 반응형 디자인 (모바일/태블릿/PC 최적화)
- 애니메이션 효과 (페이드인, 하트 비트, 플로팅 등)
- 마음 전할 곳 (계좌번호 클릭 시 복사)
- 결혼식 동영상 재생
- 실시간 댓글 시스템 (백엔드 연동)

## 로컬 실행

### 백엔드 서버 실행
```bash
pip install -r requirements.txt
python server.py
```
서버가 http://localhost:5000 에서 실행됩니다.

### 프론트엔드 열기
브라우저에서 `wedding_invitation_react.html` 파일을 열거나:
```bash
python -c "import webbrowser; webbrowser.open('wedding_invitation_react.html')"
```

## 배포 방법

### 1. Render 배포 (권장)
1. GitHub에 프로젝트 업로드
2. [Render](https://render.com) 가입
3. New Web Service 생성
4. GitHub 리포지토리 연결
5. Runtime: Python 3
6. Build Command: `pip install -r requirements.txt`
7. Start Command: `gunicorn server:app`
8. 배포 완료 후 URL 확인

### 2. 임시 터널링 (ngrok)
```bash
pip install pyngrok
python server.py  # 한 터미널에서 서버 실행
python tunnel.py  # 다른 터미널에서 터널 실행
```
공개 URL이 생성됩니다.

### 3. 커스텀 도메인 설정
Render에서 배포 후 Custom Domain 설정에서 `moonjoohoggo3` 도메인 연결 가능.

## 파일 구조

- `wedding_invitation_react.html`: 메인 청첩장 페이지 (React + HTML)
- `server.py`: Flask 백엔드 서버 (댓글 API)
- `comments.json`: 댓글 데이터 저장 파일
- `requirements.txt`: Python 의존성
- `Procfile`: Heroku 스타일 프로세스 파일
- `render.yaml`: Render 배포 설정
- `tunnel.py`: ngrok 터널링 스크립트
- `marriage.py`: 청첩장 HTML 생성 스크립트

## API 엔드포인트

- `GET /api/comments`: 댓글 목록 조회
- `POST /api/comments`: 새 댓글 추가 (JSON: {name, message})

## 기술 스택

- **프론트엔드**: React 18 (CDN), Babel, CSS3 애니메이션
- **백엔드**: Flask, Flask-CORS
- **데이터 저장**: JSON 파일 (데이터베이스로 확장 가능)

## 확장 가능성

- 데이터베이스 연동 (SQLite, PostgreSQL 등)
- 사용자 인증
- 이메일 알림
- 사진 갤러리
- RSVP 기능

- Python 3.x
- Dependencies listed in requirements.txt

## Note

This is a basic prediction model for demonstration purposes. Real stock prediction requires more sophisticated models and should not be used for actual trading decisions.