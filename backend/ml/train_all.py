import pandas as pd
import joblib

from sentence_transformers import SentenceTransformer
from sklearn.linear_model import LogisticRegression

print("Loading Dataset...")

df = pd.read_csv("dataset/requirements_dataset.csv")

embedder = SentenceTransformer("all-MiniLM-L6-v2")

print("Generating Embeddings...")

embeddings = embedder.encode(df["requirement"].tolist(), show_progress_bar=True)

targets = {
    "domain": "domain_classifier.pkl",
    "complexity": "complexity_classifier.pkl",
    "timeline": "timeline_classifier.pkl",
    "budget": "budget_classifier.pkl"
}

for column, filename in targets.items():

    print(f"\nTraining {column} model...")

    model = LogisticRegression(max_iter=1000)

    model.fit(embeddings, df[column])

    joblib.dump(model, f"models/{filename}")

print("\nSaving Embedder...")

joblib.dump(embedder, "models/embedder.pkl")

print("\nALL MODELS TRAINED SUCCESSFULLY!")