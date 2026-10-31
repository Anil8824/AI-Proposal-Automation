import os
import joblib

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_ROOT = os.path.dirname(CURRENT_DIR)

MODEL_DIR = os.path.join(PROJECT_ROOT, "ml", "models")

print("MODEL_DIR =", MODEL_DIR)
print("Exists?", os.path.exists(MODEL_DIR))

embedder = joblib.load(os.path.join(MODEL_DIR, "embedder.pkl"))
domain_model = joblib.load(os.path.join(MODEL_DIR, "domain_classifier.pkl"))
complexity_model = joblib.load(os.path.join(MODEL_DIR, "complexity_classifier.pkl"))
timeline_model = joblib.load(os.path.join(MODEL_DIR, "timeline_classifier.pkl"))
budget_model = joblib.load(os.path.join(MODEL_DIR, "budget_classifier.pkl"))

# --------------------------------------------------
# Analyze Requirement
# --------------------------------------------------

def analyze_requirement(text):

    embedding = embedder.encode([text])

    return {
        "domain": domain_model.predict(embedding)[0],
        "complexity": complexity_model.predict(embedding)[0],
        "timeline": timeline_model.predict(embedding)[0],
        "budget": budget_model.predict(embedding)[0]
    }