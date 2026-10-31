import joblib

from sentence_transformers import SentenceTransformer

embedder = joblib.load("models/embedder.pkl")
classifier = joblib.load("models/domain_classifier.pkl")


while True:

    text = input("\nRequirement : ")

    embedding = embedder.encode([text])

    prediction = classifier.predict(embedding)

    print("\nPredicted Domain :", prediction[0])