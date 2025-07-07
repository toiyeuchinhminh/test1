from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Xin chào! Tôi là Nguyễn Tấn Tài - 2212991."

if __name__ == '__main__':
    app.run(port=5000)
