from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://admin:123456@localhost:27018")
db = client["membership_db"]
members_collection = db["members"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register-page")
def register_page():
    return render_template("register.html")

@app.route("/api/members", methods=["GET"])
def get_members():
    members = list(members_collection.find({}, {"_id": 0}))

    return jsonify(members)

@app.route("/api/member/search", methods=["GET"])
def search_member():
    email = request.args.get("email")

    member = members_collection.find_one(
        {"email": email},
        {"_id": 0}
    )

    if member:
        return jsonify(member)
    else:
        return jsonify({"message": "查無此會員"}), 404

@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    phone = data.get("phone")

    if not email or not phone:
        return jsonify({"message": "請輸入 Email 和手機"}), 400

    member = members_collection.find_one(
        {"email": email, "phone": phone},
        {"_id": 0}
    )

    if member:
        return jsonify({
            "message": "登入成功",
            "member": member
        })
    else:
        return jsonify({"message": "Email 或手機錯誤"}), 401

@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()

    name = data.get("name")
    birthday = data.get("birthday")
    phone = data.get("phone")
    email = data.get("email")

    # 🔥 檢查是否有空欄位
    if not name or not birthday or not phone or not email:
        return jsonify({"message": "請填寫完整資料"}), 400

    # 🔥 檢查 Email 是否重複
    if members_collection.find_one({"email": email}):
        return jsonify({"message": "Email 已被註冊"}), 400

    # 🔥 檢查手機是否重複
    if members_collection.find_one({"phone": phone}):
        return jsonify({"message": "手機已被註冊"}), 400

    # 建立會員
    member = {
        "name": name,
        "birthday": birthday,
        "phone": phone,
        "email": email,
        "status": "active",
        "level": "basic",
        "points": 0
    }

    members_collection.insert_one(member)

    return jsonify({"message": "註冊成功"})

if __name__ == "__main__":
    app.run(debug=True, port=5001)