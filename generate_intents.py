import random

templates = {
    "greeting": [
        "xin chào", "chào bạn", "hello", "hi", "chào shop",
        "shop ơi", "alo", "chào buổi sáng", "chào buổi tối"
    ],

    "thanks": [
        "cảm ơn", "thanks", "cảm ơn shop", "ok cảm ơn", "thank you"
    ],

    "goodbye": [
        "tạm biệt", "bye", "hẹn gặp lại", "chào nhé"
    ],

    "size": [
        "tôi cao {h} nặng {w}kg",
        "cao {h}cm nặng {w}",
        "với chiều cao {h} cân nặng {w} thì mặc size gì",
        "tư vấn size cho người cao {h} nặng {w}"
    ],

    "product": [
        "shop có bán áo không",
        "có quần không",
        "có váy không",
        "có áo sơ mi không",
        "có đồ nữ không"
    ],

    "price": [
        "giá bao nhiêu",
        "bao nhiêu tiền",
        "giá sản phẩm này",
        "áo này giá bao nhiêu"
    ],

    "fashion": [
        "phối đồ đi chơi",
        "phối đồ đi làm",
        "phối đồ đẹp",
        "phối đồ cho nữ"
    ],

    "style": [
        "mặc gì đi tiệc",
        "mặc gì đi chơi",
        "mặc gì cho nữ",
        "mặc gì cho nam"
    ],

    "shipping": [
        "shop có giao hàng không",
        "ship mất bao lâu",
        "giao hàng trong mấy ngày"
    ],

    "policy": [
        "có đổi trả không",
        "chính sách đổi trả",
        "đổi size được không"
    ]
}

heights = range(145, 185)
weights = range(40, 90)

output = []

for intent, sentences in templates.items():
    output.append(f"[{intent}]")

    for _ in range(120):   # 120 x 8 intents ≈ 960 câu
        s = random.choice(sentences)

        if "{h}" in s:
            s = s.replace("{h}", str(random.choice(heights)))
        if "{w}" in s:
            s = s.replace("{w}", str(random.choice(weights)))

        output.append(s)

with open("intents.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(output))

print("Đã tạo intents.txt ~1000 câu hỏi!")
