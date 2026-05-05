# database.py = 專門負責「連 MongoDB + 提供資料表」


from pymongo import MongoClient
# 讓 Python 可以連 MongoDB

# 在 docker-compose 裡，Flask 容器不能用 localhost 連 MongoDB，要用 service 名稱（mongo）
# 要用 MongoDB 服務名稱 mongo 當作主機名稱
client = MongoClient("mongodb://admin:123456@mongo:27017")
# 連到 Docker 裡的 MongoDB（名字叫 mongo、帳號admin、密碼123456、port27017）

db = client["membership_db"]
# 使用（或建立）一個資料庫叫 membership_db

members_collection = db["members"]
# 使用（或建立）一個 collection 叫 members