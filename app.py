from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://admin:123456@localhost:27018")
db = client["membership_db"]
members_collection = db["members"]

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")

    member = {
        "name": name,
        "email": email,
        "status": "active",
        "level": "basic",
        "points": 0
    }

    members_collection.insert_one(member)

    return jsonify({
        "message": "註冊成功，已存進 MongoDB",
        "name": name,
        "email": email
    })

@app.route("/api/members", methods=["GET"])
def get_members():
    members = list(members_collection.find({}, {"_id": 0}))

    return jsonify(members)

if __name__ == "__main__":
    app.run(debug=True, port=5001)