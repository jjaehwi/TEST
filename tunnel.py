from pyngrok import ngrok
import time

# ngrok 터널 시작 (포트 5000)
public_url = ngrok.connect(5000)
print(f"공개 URL: {public_url}")

# 서버 실행 (별도 터미널에서 python server.py 실행 필요)
print("서버를 실행한 후 이 스크립트를 실행하세요.")
print("Ctrl+C로 중지")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    ngrok.disconnect(public_url)
    print("터널 종료")