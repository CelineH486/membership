# 功能說明：會員資料庫操作（Repository 層）
# 負責與 MongoDB 溝通（查詢 / 新增資料）


from database import members_collection


# 取得所有會員資料
def get_all_members():
    return list(members_collection.find({}, {"_id": 0}))


# 根據 Email 查詢會員
def find_member_by_email(email):
    return members_collection.find_one({"email": email}, {"_id": 0})


# 根據手機查詢會員
def find_member_by_phone(phone):
    return members_collection.find_one({"phone": phone}, {"_id": 0})


def find_member_by_email_and_phone(email, phone):
    return members_collection.find_one(
        {"email": email, "phone": phone},
        {"_id": 0}
    )


# 新增會員資料（註冊用）
def create_member(member):
    members_collection.insert_one(member)


# Repository = 專門負責查資料庫，不做邏輯判斷