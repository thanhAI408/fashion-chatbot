import random

intents = {
    "greeting": [
        "hello", "hi", "chào", "chào bạn", "xin chào", "chào shop",
        "alo", "hey", "chào buổi sáng", "chào buổi tối"
    ],
    "goodbye": [
        "tạm biệt", "bye", "hẹn gặp lại", "chào nhé", "chúc shop vui"
    ],
    "thanks": [
        "cảm ơn", "thanks", "cảm ơn nhiều", "rất cảm ơn", "ok cảm ơn"
    ],
    "product": [
        "shop có áo không", "shop bán quần không", "có váy không",
        "mình muốn mua áo", "mình muốn xem sản phẩm"
    ],
    "price": [
        "giá bao nhiêu", "áo này giá bao nhiêu", "bao nhiêu tiền",
        "mắc không", "giá thế nào"
    ],
    "fashion": [
        "phối đồ sao cho đẹp", "tư vấn phong cách", "mặc sao cho đẹp",
        "gợi ý phối đồ", "tư vấn thời trang"
    ],
    "style": [
        "phong cách trẻ trung", "phong cách công sở",
        "phong cách cá tính", "style hàn quốc", "style vintage"
    ],
    "shipping": [
        "ship không", "giao hàng không", "bao lâu nhận được",
        "có ship cod không", "phí ship bao nhiêu"
    ],
    "policy": [
        "đổi trả thế nào", "chính sách bảo hành",
        "có được trả hàng không", "đổi size được không",
        "chính sách shop thế nào"
    ]
}

def expand(sentence):
    variants = [
        sentence,
        "cho mình hỏi " + sentence,
        "mình muốn biết " + sentence,
        sentence + " vậy",
        sentence + " ạ",
        "shop ơi " + sentence,
        "bạn ơi " + sentence
    ]
    return variants

output = ""

for intent, samples in intents.items():
    output += f"\n[{intent}]\n"
    all_sentences = []
    for s in samples:
        all_sentences.extend(expand(s))

    random.shuffle(all_sentences)
    all_sentences = list(set(all_sentences))

    while len(all_sentences) < 550:
        base = random.choice(samples)
        all_sentences.append(random.choice(expand(base)))

    for s in all_sentences[:550]:
        output += s + "\n"

with open("intentsmore.txt", "w", encoding="utf-8") as f:
    f.write(output)

print("Đã tạo intentssmore.txt ~ 5000 câu")
