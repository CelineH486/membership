# 功能說明：會員相關 API 控制器（Controller）
# 負責接收前端請求，呼叫 Service 處理邏輯，並回傳結果

from flask import Blueprint, request, jsonify, session
from services.member_service import (
    get_members_service,
    search_member_service,
    login_service,
    register_service
)

# 建立 Blueprint（API 分組）
member_bp = Blueprint("member", __name__)


# API：取得全部會員
@member_bp.route("/api/members", methods=["GET"])
def get_members():
    members = get_members_service()
    return jsonify(members)


# API：查詢目前登入會員資料
@member_bp.route("/api/member/search", methods=["GET"])
def search_member():
    # 檢查是否已登入（透過 session）
    if "member_email" not in session:
        return jsonify({"message": "請先登入"}), 401

    # 不再使用前端傳來的 email
    # 改用 session 裡的 email
    email = session["member_email"]

    # 呼叫 Service 查詢會員資料
    result, status_code = search_member_service(email)
    return jsonify(result), status_code


# API：會員登入
@member_bp.route("/api/login", methods=["POST"])
def login():
    # 取得前端傳來的 JSON 資料（email, phone）
    data = request.get_json()

    # 呼叫 service 做驗證
    result, status_code = login_service(data)

    # 如果登入成功 → 將會員 email 存入 session（建立登入狀態）
    if status_code == 200:
        session["member_email"] = result["member"]["email"]

    return jsonify(result), status_code


# API：會員註冊
@member_bp.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()
    result, status_code = register_service(data)
    return jsonify(result), status_code


# API：檢查登入狀態（看 cookie / session）
@member_bp.route("/api/me", methods=["GET"])
def me():
    # 如果沒有 session → 代表尚未登入
    if "member_email" not in session:
        return jsonify({"message": "尚未登入"}), 401

    # 有 session → 回傳目前登入者資訊
    return jsonify({
        "message": "已登入",
        "email": session["member_email"]
    }), 200


# API：登出
@member_bp.route("/api/logout", methods=["POST"])
def logout():
    # 清除 session（登出）
    session.clear()
    return jsonify({"message": "已登出"}), 200