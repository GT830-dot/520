from flask import Flask, render_template, jsonify
import datetime

app = Flask(__name__)

# 表白文案库
love_messages = [
    "520快乐！遇见你，是我最美丽的意外。",
    "你是我眼中最美的风景，心中最暖的阳光。",
    "我想把世界上最好的都给你，却发现世界上最好的就是你。",
    "你笑的时候，全世界都在发光。",
    "余生很长，请多指教。",
    "我想牵着你的手，走过每一个春夏秋冬。",
    "你是我写过最美的情书，也是我做过最美的梦。",
    "喜欢你这件事，大概会持续一辈子吧。",
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/love')
def get_love():
    today = datetime.date.today()
    msg_index = today.day % len(love_messages)
    return jsonify({
        'message': love_messages[msg_index],
        'date': today.strftime('%Y年%m月%d日'),
        'total_days': (today - datetime.date(2024, 1, 1)).days
    })

@app.route('/api/countdown')
def countdown():
    today = datetime.date.today()
    next_520 = datetime.date(today.year, 5, 20)
    if today > next_520:
        next_520 = datetime.date(today.year + 1, 5, 20)
    days_left = (next_520 - today).days
    return jsonify({
        'days_left': days_left,
        'next_520': next_520.strftime('%Y年%m月%d日')
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5200)
