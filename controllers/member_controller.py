from flask import Blueprint, request, jsonify, session
from services.member_service import (
    get_members_service,
    search_member_service,
    login_service,
    register_service
)

# 建立 Blueprint（API 分組）
member_bp = Blueprint("member", __name__)


# 取得全部會員
@member_bp.route("/api/members", methods=["GET"])
def get_members():
    members = get_members_service()
    return jsonify(members)


# 查詢會員
@member_bp.route("/api/member/search", methods=["GET"])
def search_member():
    # 先檢查有沒有登入
    if "member_email" not in session:
        return jsonify({"message": "請先登入"}), 401

    # 不再使用前端傳來的 email
    # 改用 session 裡的 email（安全）
    email = session["member_email"]

    result, status_code = search_member_service(email)
    return jsonify(result), status_code


# 登入
@member_bp.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()

    # 呼叫 service 做驗證
    result, status_code = login_service(data)

    # 如果登入成功 → 存 session（重點！）
    if status_code == 200:
        session["member_email"] = result["member"]["email"]

    return jsonify(result), status_code


# 註冊
@member_bp.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()
    result, status_code = register_service(data)
    return jsonify(result), status_code


# 檢查登入狀態（看 cookie / session）
@member_bp.route("/api/me", methods=["GET"])
def me():
    # 如果沒有 session → 代表沒登入
    if "member_email" not in session:
        return jsonify({"message": "尚未登入"}), 401

    # 有 session → 回傳目前登入者
    return jsonify({
        "message": "已登入",
        "email": session["member_email"]
    }), 200


# 登出（清除 session）
@member_bp.route("/api/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"message": "已登出"}), 200