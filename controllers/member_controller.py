from flask import Blueprint, request, jsonify
from services.member_service import (
    get_members_service,
    search_member_service,
    login_service,
    register_service
)

member_bp = Blueprint("member", __name__)


@member_bp.route("/api/members", methods=["GET"])
def get_members():
    members = get_members_service()
    return jsonify(members)


@member_bp.route("/api/member/search", methods=["GET"])
def search_member():
    email = request.args.get("email")
    result, status_code = search_member_service(email)
    return jsonify(result), status_code


@member_bp.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    result, status_code = login_service(data)
    return jsonify(result), status_code


@member_bp.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()
    result, status_code = register_service(data)
    return jsonify(result), status_code