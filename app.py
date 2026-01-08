from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

model = joblib.load("intent_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    X = vectorizer.transform([user_input])
    intent = model.predict(X)[0]

    if intent == "size":
        reply = "Bạn hãy nhập chiều cao và cân nặng để mình tư vấn size nhé."
    elif intent == "fashion":
        reply = "Mình có thể tư vấn phối đồ, kiểu dáng và phong cách cho bạn."
    else:
        reply = "Xin lỗi, mình chỉ hỗ trợ tư vấn về thời trang."

    return jsonify({"reply": reply})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
