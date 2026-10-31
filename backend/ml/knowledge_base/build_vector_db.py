import os
import json
import chromadb

from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create persistent ChromaDB client
client = chromadb.PersistentClient(path="../vector_db")

# Delete old collection if it exists
try:
    client.delete_collection("projects")
except:
    pass

collection = client.create_collection("projects")

# Load projects
with open("projects.json", "r", encoding="utf-8") as f:
    projects = json.load(f)

print(f"Loaded {len(projects)} projects")

for idx, project in enumerate(projects):

    text = f"""
Title: {project['title']}
Domain: {project['domain']}
Summary: {project['summary']}
Technology: {', '.join(project['tech_stack'])}
"""

    embedding = model.encode(text).tolist()

    collection.add(
        ids=[str(idx)],
        documents=[text],
        embeddings=[embedding],
        metadatas=[project]
    )

print("✅ Vector Database Created Successfully!")