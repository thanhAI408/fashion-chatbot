# Lưu ý khi train dât thì cần copy tất cả data từ nguồn nào đó sau đó dán ô đầu tiên
# trong excel sau đó chuyển text thành cột ngăn cách bởi dấu phẩy là xong.

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

texts = []
labels = []

current_intent = None

# ====== ĐỌC DATASET ======
with open("intents.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip().lower()

        if not line:
            continue

        if line.startswith("[") and line.endswith("]"):
            current_intent = line[1:-1]
        else:
            texts.append(line)
            labels.append(current_intent)

print("Tổng câu trước khi lọc:", len(texts))

# ====== LOẠI BỎ TRÙNG ======
unique_data = {}
for text, label in zip(texts, labels):
    if text not in unique_data:
        unique_data[text] = label

texts = list(unique_data.keys())
labels = list(unique_data.values())

print("Tổng câu sau khi lọc trùng:", len(texts))

# ====== SPLIT TRAIN / TEST ======
X_train, X_test, y_train, y_test = train_test_split(
    texts, labels,
    test_size=0.2,
    random_state=42,
    stratify=labels
)

# ====== TF-IDF ======
vectorizer = TfidfVectorizer(
    ngram_range=(1,2),
    min_df=1,
    max_df=0.9
)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# ====== MODEL ======
model = LogisticRegression(
    max_iter=2000,
    solver="lbfgs"
)

model.fit(X_train_vec, y_train)

# ====== ĐÁNH GIÁ ======
y_pred = model.predict(X_test_vec)

acc = accuracy_score(y_test, y_pred)

print("\n========== MODEL EVALUATION ==========")
print("Accuracy:", round(acc, 4))

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

# ====== SAVE ======
joblib.dump(model, "intent_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("\nĐã lưu model và vectorizer!")
