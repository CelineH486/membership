// 查詢全部會員並顯示在畫面

// 🟢 取得所有會員並顯示在畫面
function getMembers() {

    // 🟢 呼叫後端 API（取得會員列表）
    fetch("/api/members")

    // 🟢 將回傳資料轉為 JSON
    .then(res => res.json())

    // 🟢 處理資料
    .then(data => {
        const list = document.getElementById("memberList");

        // 🟢 清空原本內容（避免重複）
        list.innerHTML = "";

        // 🟢 一筆一筆建立列表
        data.forEach(member => {
            const li = document.createElement("li");

            // 🟢 顯示姓名 + Email
            li.textContent = member.name + " - " + member.email;

            // 🟢 加到畫面上
            list.appendChild(li);
        });
    });
}