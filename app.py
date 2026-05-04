from flask import Flask, render_template
from controllers.member_controller import member_bp

app = Flask(__name__)

app.register_blueprint(member_bp)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register-page")
def register_page():
    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)