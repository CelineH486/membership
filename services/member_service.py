from repositories.member_repository import (
    get_all_members,
    find_member_by_email,
    find_member_by_phone,
    find_member_by_email_and_phone,
    create_member
)


def get_members_service():
    return get_all_members()


def search_member_service(email):
    if not email:
        return {"message": "請輸入 Email"}, 400

    member = find_member_by_email(email)

    if member:
        return member, 200
    else:
        return {"message": "查無此會員"}, 404


def login_service(data):
    email = data.get("email")
    phone = data.get("phone")

    if not email or not phone:
        return {"message": "請輸入 Email 和手機"}, 400

    member = find_member_by_email_and_phone(email, phone)

    if member:
        return {
            "message": "登入成功",
            "member": member
        }, 200
    else:
        return {"message": "Email 或手機錯誤"}, 401


def register_service(data):
    name = data.get("name")
    birthday = data.get("birthday")
    phone = data.get("phone")
    email = data.get("email")

    if not name or not birthday or not phone or not email:
        return {"message": "請填寫完整資料"}, 400

    if find_member_by_email(email):
        return {"message": "Email 已被註冊"}, 400

    if find_member_by_phone(phone):
        return {"message": "手機已被註冊"}, 400

    member = {
        "name": name,
        "birthday": birthday,
        "phone": phone,
        "email": email,
        "status": "active",
        "level": "basic",
        "points": 0
    }

    create_member(member)

    return {"message": "註冊成功"}, 200