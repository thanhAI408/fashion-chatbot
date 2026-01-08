import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

data = pd.read_csv("intents.csv")

X = data["text"]
y = data["intent"]

vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vec, y)

joblib.dump(model, "intent_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Train xong model chatbot!")
