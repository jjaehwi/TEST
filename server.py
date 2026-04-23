from flask import Flask, request, jsonify, send_file, render_template_string
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

COMMENTS_FILE = 'comments.json'
WEDDING_FILE = 'wedding_invitation_react.html'

def load_comments():
    if os.path.exists(COMMENTS_FILE):
        with open(COMMENTS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_comments(comments):
    with open(COMMENTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(comments, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    """청첩장 메인 페이지"""
    try:
        with open(WEDDING_FILE, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "청첩장 파일을 찾을 수 없습니다.", 404

@app.route('/api/comments', methods=['GET'])
def get_comments():
    """댓글 목록 조회"""
    comments = load_comments()
    return jsonify(comments)

@app.route('/api/comments', methods=['POST'])
def add_comment():
    """새 댓글 추가"""
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
    try:
        from waitress import serve
        print("서버가 http://0.0.0.0:5000 에서 실행 중입니다...")
        serve(app, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    except ImportError:
        print("gunicorn으로 실행")
        app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))