from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import os
import random

app = Flask(__name__)

model = joblib.load("intent_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

RESPONSES = {
    "greeting": [
        "Chào bạn 👋 Mình là trợ lý thời trang, mình có thể giúp gì cho bạn?",
        "Xin chào! Bạn đang muốn tư vấn quần áo hay phong cách?"
    ],
    "thanks": [
        "Rất vui được hỗ trợ bạn 😊",
        "Cảm ơn bạn đã tin tưởng mình!"
    ],
    "goodbye": [
        "Tạm biệt bạn 👋 Hẹn gặp lại nhé!",
        "Chúc bạn một ngày vui vẻ!"
    ],
    "size": [
        "Bạn cho mình chiều cao, cân nặng và giới tính để mình tư vấn size chuẩn nhé.",
        "Bạn cao bao nhiêu cm và nặng bao nhiêu kg để mình chọn size phù hợp?"
    ],
    "product": [
        "Bạn đang quan tâm áo, quần hay váy để mình gợi ý cho bạn?",
        "Mình có nhiều mẫu đẹp, bạn muốn xem loại nào?"
    ],
    "price": [
        "Bạn cho mình biết sản phẩm bạn quan tâm để mình báo giá chính xác nhé.",
        "Khoảng giá bạn mong muốn là bao nhiêu?"
    ],
    "fashion": [
        "Bạn muốn phối đồ theo phong cách nào: trẻ trung, công sở hay cá tính?",
        "Mình có thể gợi ý set đồ phù hợp với bạn."
    ],
    "style": [
        "Bạn cho mình biết hoàn cảnh để mình gợi ý trang phục phù hợp nhé.",
        "Bạn là nam hay nữ để mình tư vấn chính xác hơn?"
    ],
    "shipping": [
        "Shop có giao hàng toàn quốc, thời gian từ 2–4 ngày bạn nhé.",
        "Shop hỗ trợ ship COD toàn quốc."
    ],
    "policy": [
        "Shop hỗ trợ đổi trả trong 7 ngày nếu sản phẩm lỗi hoặc không vừa size.",
        "Bạn có thể đổi trả theo chính sách của shop trong 7 ngày."
    ]
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    X = vectorizer.transform([user_input])
    probs = model.predict_proba(X)[0]

    best_index = np.argmax(probs)
    confidence = probs[best_index]
    intent = model.classes_[best_index]

    if confidence < 0.35:
        reply = "Mình chỉ hỗ trợ tư vấn về thời trang, bạn hỏi lại giúp mình rõ hơn nhé 👗"
    else:
        reply = random.choice(RESPONSES.get(intent, [
            "Mình chưa hiểu rõ, bạn hỏi lại giúp mình nhé."
        ]))

    return jsonify({
        "reply": reply,
        "intent": intent,
        "confidence": round(float(confidence), 2)
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
