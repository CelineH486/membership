from pymongo import MongoClient

# 在 docker-compose 裡，Flask 容器不能用 localhost 連 MongoDB
# 要用 MongoDB 服務名稱 mongo 當作主機名稱
client = MongoClient("mongodb://admin:123456@mongo:27017")

db = client["membership_db"]

members_collection = db["members"]