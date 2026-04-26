from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")

    print("收到註冊資料:", name, email)

    return jsonify({
        "message": "註冊成功",
        "name": name,
        "email": email
    })


if __name__ == "__main__":
    app.run(debug=True, port=5001)