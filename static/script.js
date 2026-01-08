function addMessage(text, sender) {
    let box = document.getElementById("chatBox");

    let div = document.createElement("div");
    div.className = sender;

    let bubble = document.createElement("div");
    bubble.className = "bubble";
    bubble.innerText = text;

    div.appendChild(bubble);
    box.appendChild(div);

    box.scrollTop = box.scrollHeight;
}

function sendMessage() {
    let input = document.getElementById("userInput");
    let text = input.value.trim();
    if (!text) return;

    addMessage(text, "user");
    input.value = "";

    fetch("/chat", {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({message:text})
    })
    .then(res=>res.json())
    .then(data=>{
        addMessage(data.reply, "bot");
    });
}

function handleKey(e){
    if(e.key==="Enter") sendMessage();
}
