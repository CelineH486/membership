FROM python:3.11-slim
# 用 Python 3.11 的精簡版當作基礎環境

WORKDIR /app
# 設定容器裡面的工作資料夾為 /app

COPY requirements.txt .
# 把本機的 requirements.txt 複製到容器目前資料夾

RUN pip install --no-cache-dir -r requirements.txt
# 根據 requirements.txt 安裝需要的 Python 套件

COPY . .
# 把整個專案的檔案複製到容器目前資料夾

EXPOSE 5001
# 告訴 Docker 這個程式會使用 5001 port

CMD ["python", "app.py"]
# 容器啟動時執行 python app.py