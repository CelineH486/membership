# 啟動 Flask + 設定路由 + 接上 Controller


from flask import Flask, render_template
from controllers.member_controller import member_bp
# Flask → 建網站用
# render_template → 顯示 HTML 頁面
# member_bp = 寫好的 API（在 controller）

# 建立一個網站（Flask 應用）
app = Flask(__name__)

# 設定 Session 金鑰，讓 Flask 可以用 session（登入狀態）
app.secret_key = "membership-secret-key"

# 註冊 Blueprint
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
    # 讓 Docker 外部可以連線
    app.run(host="0.0.0.0", debug=True, port=5001)