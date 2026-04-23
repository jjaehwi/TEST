from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__, static_folder='.')
CORS(app)  # 모든 도메인에서 접근 허용

COMMENTS_FILE = 'comments.json'

def load_comments():
    if os.path.exists(COMMENTS_FILE):
        with open(COMMENTS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_comments(comments):
    with open(COMMENTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(comments, f, ensure_ascii=False, indent=2)

@app.route('/', methods=['GET'])
def index():
    return '''
    <h1>청첩장 백엔드 서버</h1>
    <p>서버가 정상 작동 중입니다.</p>
    <h2>API 엔드포인트</h2>
    <ul>
        <li><a href="/api/comments">GET /api/comments</a> - 댓글 목록 조회</li>
        <li>POST /api/comments - 새 댓글 추가</li>
    </ul>
    <p>청첩장 파일: <a href="wedding_invitation_react.html">wedding_invitation_react.html</a></p>
    '''

@app.route('/wedding')
def wedding():
    return app.send_static_file('wedding_invitation_react.html')

@app.route('/api/comments', methods=['GET'])
def get_comments():
    comments = load_comments()
    return jsonify(comments)

@app.route('/api/comments', methods=['POST'])
def add_comment():
    data = request.get_json()
    name = data.get('name', '').strip()
    message = data.get('message', '').strip()

    if not name or not message:
        return jsonify({'error': '이름과 메시지를 모두 입력해주세요.'}), 400

    comments = load_comments()
    new_comment = {
        'id': len(comments) + 1,
        'name': name,
        'message': message,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    comments.append(new_comment)
    save_comments(comments)

    return jsonify(new_comment), 201

if __name__ == '__main__':
    # Windows에서는 waitress 사용, 다른 OS에서는 gunicorn
    try:
        from waitress import serve
        print("Windows에서 waitress로 서버 실행")
        serve(app, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    except ImportError:
        print("gunicorn으로 서버 실행")
        app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))