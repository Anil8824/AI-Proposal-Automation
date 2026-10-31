import pandas as pd
import joblib

from sentence_transformers import SentenceTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

print("Loading dataset...")

df = pd.read_csv("dataset/requirements_dataset.csv")

X = df["requirement"]
y = df["domain"]

print("Generating embeddings...")

embedder = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = embedder.encode(
    X.tolist(),
    show_progress_bar=True
)

X_train, X_test, y_train, y_test = train_test_split(
    embeddings,
    y,
    test_size=0.2,
    random_state=42
)

print("Training classifier...")

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

pred = model.predict(X_test)

accuracy = accuracy_score(y_test, pred)

print("\nAccuracy:", accuracy)

joblib.dump(model, "models/domain_classifier.pkl")
joblib.dump(embedder, "models/embedder.pkl")

print("\nSaved Successfully!")