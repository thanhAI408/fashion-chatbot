# Lưu ý khi train dât thì cần copy tất cả data từ nguồn nào đó sau đó dán ô đầu tiên
# trong excel sau đó chuyển text thành cột ngăn cách bởi dấu phẩy là xong.

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

texts = []
labels = []

current_intent = None

with open("intents.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        if line.startswith("[") and line.endswith("]"):
            current_intent = line[1:-1]
        else:
            texts.append(line)
            labels.append(current_intent)

vectorizer = TfidfVectorizer(ngram_range=(1,2))
X = vectorizer.fit_transform(texts)

model = LogisticRegression(max_iter=1000)
model.fit(X, labels)

joblib.dump(model, "intent_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Train xong với intents.txt!")
