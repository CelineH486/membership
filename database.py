from pymongo import MongoClient

client = MongoClient("mongodb://admin:123456@localhost:27018")

db = client["membership_db"]

members_collection = db["members"]