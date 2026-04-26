function getMembers() {
    fetch("/api/members")
    .then(res => res.json())
    .then(data => {
        const list = document.getElementById("memberList");
        list.innerHTML = "";

        data.forEach(member => {
            const li = document.createElement("li");
            li.textContent = member.name + " - " + member.email;
            list.appendChild(li);
        });
    });
}