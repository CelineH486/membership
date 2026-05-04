from database import members_collection


def get_all_members():
    return list(members_collection.find({}, {"_id": 0}))


def find_member_by_email(email):
    return members_collection.find_one({"email": email}, {"_id": 0})


def find_member_by_phone(phone):
    return members_collection.find_one({"phone": phone}, {"_id": 0})


def find_member_by_email_and_phone(email, phone):
    return members_collection.find_one(
        {"email": email, "phone": phone},
        {"_id": 0}
    )


def create_member(member):
    members_collection.insert_one(member)