/* 1. DỮ LIỆU SẢN PHẨM (LOCAL IMAGES) */
const products = [
    {
        id: 1,
        name: "Cyberpunk Bomber Jacket",
        category: "streetwear",
        price: 850000,
        img: "/static/products/shirt1.jpg", 
        desc: "Áo khoác phong cách tương lai, chất liệu phản quang, chống nước."
    },
    {
        id: 2,
        name: "Neon Silk Evening Dress",
        category: "formal",
        price: 1200000,
        img: "/static/products/dress1.jpg",
        desc: "Váy lụa cao cấp, cắt xẻ táo bạo, tôn dáng hoàn hảo cho các bữa tiệc."
    },
    {
        id: 3,
        name: "Techwear Cargo Pants",
        category: "streetwear",
        price: 550000,
        img: "/static/products/quan1.jpg",
        desc: "Quần túi hộp đa năng, vải dù siêu nhẹ, phong cách Techwear."
    },
    {
        id: 4,
        name: "Holo-Graphic Tee",
        category: "casual",
        price: 320000,
        img: "/static/products/dress2.jpg",
        desc: "Áo thun in họa tiết Hologram đổi màu theo góc nhìn."
    },
    {
        id: 5,
        name: "Minimalist Blazer",
        category: "formal",
        price: 950000,
        img: "/static/products/dress3.jpg",
        desc: "Blazer cắt may thủ công, phong cách tối giản sang trọng."
    },
    {
        id: 6,
        name: "Street Oversized Hoodie",
        category: "casual",
        price: 450000,
        img: "/static/products/dress4.jpg",
        desc: "Hoodie form rộng thoải mái, chất nỉ bông ấm áp."
    }
];

const productGrid = document.getElementById("productGrid");
const cartCount = document.getElementById("cartCount");
let cart = 0;

/* 2. RENDER SẢN PHẨM */
function renderProducts(filter = "all") {
    productGrid.innerHTML = "";
    products.forEach(p => {
        if (filter === "all" || p.category === filter) {
            const card = document.createElement("div");
            card.className = "product-card";
            card.onclick = () => openModal(p);
            
            const priceStr = new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(p.price);

            card.innerHTML = `
                <div class="img-box">
                    <img src="${p.img}" alt="${p.name}">
                </div>
                <div class="info-box">
                    <span class="p-cat">${p.category}</span>
                    <h3 class="p-name">${p.name}</h3>
                    <span class="p-price">${priceStr}</span>
                </div>
            `;
            productGrid.appendChild(card);
        }
    });
}

// Khởi chạy lần đầu
renderProducts();

/* 3. BỘ LỌC (FILTER) */
const filterBtns = document.querySelectorAll(".filter-btn");
filterBtns.forEach(btn => {
    btn.addEventListener("click", () => {
        document.querySelector(".filter-btn.active").classList.remove("active");
        btn.classList.add("active");
        renderProducts(btn.dataset.filter);
    });
});

/* 4. MODAL & CART LOGIC */
const modal = document.getElementById("productModal");
let currentProduct = null;

function openModal(p) {
    currentProduct = p;
    document.getElementById("modalImg").src = p.img;
    document.getElementById("modalName").innerText = p.name;
    document.getElementById("modalPrice").innerText = new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(p.price);
    document.getElementById("modalDesc").innerText = p.desc;
    
    modal.style.display = "flex";
}

function closeModal() {
    modal.style.display = "none";
}

function addToCart() {
    cart++;
    cartCount.innerText = cart;
    cartCount.style.transform = "scale(1.5)";
    setTimeout(() => cartCount.style.transform = "scale(1)", 200);
    alert(`Đã thêm ${currentProduct.name} vào giỏ hàng!`);
    closeModal();
}

window.onclick = function(e) {
    if (e.target == modal) closeModal();
}

/* 5. TÍNH NĂNG AI TRY-ON */
function triggerAITryOn() {
    if(!currentProduct) return;
    const confirmTry = confirm(`Bạn muốn thử bộ "${currentProduct.name}" này với AI không? \n(Hệ thống sẽ chuyển bạn đến phòng thử đồ ảo)`);
    if(confirmTry) {
        alert("Đang khởi động AI Engine...");
        // Code chuyển hướng hoặc mở popup Try-On sẽ nằm ở đây
    }
}

function scrollToShop() {
    document.getElementById("shop-area").scrollIntoView({behavior: "smooth"});
}

/* 6. CHATBOT - ĐÃ KẾT NỐI VỚI APP.PY */
function toggleChat() {
    const chatWindow = document.getElementById("chatWindow");
    chatWindow.style.display = chatWindow.style.display === "block" ? "none" : "block";
}

function handleChatKey(e) {
    if(e.key === "Enter") sendChatMessage();
}

function sendChatMessage() {
    const input = document.getElementById("chatInput");
    const msg = input.value.trim();
    if(!msg) return;

    // 1. Hiển thị tin nhắn người dùng
    appendMsg(msg, "user");
    input.value = "";

    // 2. Gửi tin nhắn về Server Flask (app.py)
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: msg }) // Key 'message' khớp với request.json["message"] trong app.py
    })
    .then(response => response.json())
    .then(data => {
        // 3. Hiển thị câu trả lời từ AI
        appendMsg(data.reply, "bot");
        
        // (Tùy chọn) Bạn có thể log độ tự tin để debug
        console.log(`Intent: ${data.intent}, Confidence: ${data.confidence}`);
    })
    .catch(error => {
        console.error("Lỗi:", error);
        appendMsg("Xin lỗi, server đang bận hoặc mất kết nối!", "bot");
    });
}

function appendMsg(text, type) {
    const div = document.createElement("div");
    div.className = `msg ${type}`;
    div.innerText = text;
    const chatBox = document.getElementById("chatMessages");
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}