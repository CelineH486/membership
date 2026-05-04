from repositories.member_repository import (
    get_all_members,
    find_member_by_email,
    find_member_by_phone,
    find_member_by_email_and_phone,
    create_member
)


# 取得全部會員
def get_members_service():
    return get_all_members()


# 查詢會員（用 email）
def search_member_service(email):
    if not email:
        return {"message": "請輸入 Email"}, 400

    member = find_member_by_email(email)

    if member:
        return member, 200
    else:
        return {"message": "查無此會員"}, 404


# 登入邏輯（驗證 Email + 手機）
def login_service(data):
    email = data.get("email")
    phone = data.get("phone")

    # 檢查欄位是否有填
    if not email or not phone:
        return {"message": "請輸入 Email 和手機"}, 400

    # 到資料庫比對
    member = find_member_by_email_and_phone(email, phone)

    if member:
        return {
            "message": "登入成功",
            "member": member
        }, 200
    else:
        return {"message": "Email 或手機錯誤"}, 401


# 註冊邏輯
def register_service(data):
    name = data.get("name")
    birthday = data.get("birthday")
    phone = data.get("phone")
    email = data.get("email")

    # 檢查欄位完整
    if not name or not birthday or not phone or not email:
        return {"message": "請填寫完整資料"}, 400

    # 檢查 Email 是否重複
    if find_member_by_email(email):
        return {"message": "Email 已被註冊"}, 400

    # 檢查手機是否重複
    if find_member_by_phone(phone):
        return {"message": "手機已被註冊"}, 400

    # 建立會員資料
    member = {
        "name": name,
        "birthday": birthday,
        "phone": phone,
        "email": email,
        "status": "active",
        "level": "basic",
        "points": 0
    }

    # 存入資料庫
    create_member(member)

    return {"message": "註冊成功"}, 200