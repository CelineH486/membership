from flask import Flask, render_template
from controllers.member_controller import member_bp

# 建立 Flask app
app = Flask(__name__)

# Session 必備：用來加密 Cookie（非常重要）
app.secret_key = "membership-secret-key"

# 註冊 Blueprint（把 controller 的 API 接進來）
app.register_blueprint(member_bp)


# 首頁
@app.route("/")
def home():
    return render_template("index.html")


# 註冊頁
@app.route("/register-page")
def register_page():
    return render_template("register.html")


if __name__ == "__main__":
    # host=0.0.0.0 → 讓 Docker 外部可以連線
    app.run(host="0.0.0.0", debug=True, port=5001)