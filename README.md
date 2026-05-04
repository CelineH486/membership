# Membership System (Flask + MongoDB + Docker)

## 📌 專案介紹
本專案為一個會員管理系統，採用 Flask 建立後端 API，並使用 MongoDB 作為資料庫，
透過 Docker 與 docker-compose 建立標準化執行環境。

---

## 🏗️ 系統架構
本系統採用後端三層式架構：

- Controller：負責接收 API 請求
- Service：負責商業邏輯（登入、註冊、驗證）
- Repository：負責資料庫操作（MongoDB）

---

## 🔐 認證機制
系統採用 Session（Cookie）驗證：

- 使用者登入後，後端將 email 存入 session
- 瀏覽器透過 Cookie 自動帶入 session
- 查詢會員資料時僅允許查詢自身資料

---

## 🐳 Docker 環境

本專案使用 docker-compose 同時啟動：

- Flask Web（後端服務）
- MongoDB（資料庫）

---

## 🚀 啟動方式

### 1️⃣ 下載專案

```bash
git clone <你的GitHub網址>
cd membership