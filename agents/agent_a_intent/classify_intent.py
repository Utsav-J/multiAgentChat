import os
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# === Path Setup ===
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VECTOR_INDEX_PATH = os.path.join(BASE_DIR, "vector_db", "vector.index")
METADATA_PATH = os.path.join(BASE_DIR, "vector_db", "metadata.pkl")

# === Load model, FAISS index, and metadata ===
model = SentenceTransformer("all-MiniLM-L6-v2")

print("🔄 Loading FAISS index and metadata...")
index = faiss.read_index(VECTOR_INDEX_PATH)
with open(METADATA_PATH, "rb") as f:
    metadata = pickle.load(f)
print("✅ FAISS index and metadata loaded.")

# === Similarity Threshold (cosine: 0 to 1, higher is better) ===
SIMILARITY_THRESHOLD = 0.5

def search_similar_chunks(query: str, top_k: int = 5):
    """Return top_k chunks with cosine similarity to the query."""
    # Get query embedding and normalize for cosine similarity
    query_embedding = model.encode([query], convert_to_numpy=True)
    query_embedding = query_embedding / np.linalg.norm(query_embedding, axis=1, keepdims=True)

    # Search the FAISS index
    D, I = index.search(query_embedding, top_k)

    results = []
    for score, idx in zip(D[0], I[0]):
        if idx < len(metadata):
            results.append({
                "score": float(score),  # cosine similarity
                "chunk": metadata[idx]
            })
    return results

def classify_intent(query: str):
    """
    This tool is responsible for intent classification.
    It takes in a user query and performs intent classification on it.
    It returns a well formatted json regarding whether it can answer the query or not.
    """
    results = search_similar_chunks(query, top_k=5)

    print(f"\n🔍 Top results for query: '{query}'")
    for r in results:
        print(f"🔸 Similarity: {r['score']:.4f} | Chunk: {r['chunk']['content'][:80]}...")

    avg_score = sum([r["score"] for r in results]) / len(results)
    can_answer = avg_score >= SIMILARITY_THRESHOLD

    return {
        "intent": "rag_query",
        "can_answer_from_pdf": can_answer,
        "reason": (
            f"Average cosine similarity {avg_score:.4f} with top PDF chunks."
            if can_answer else
            f"Low similarity ({avg_score:.4f}); insufficient PDF match for the query."
        )
    }

# 🧪 Example test
if __name__ == "__main__":
    # query = "Explain how inflation affects currency value."
    query = "Explain how Vision Transformer works."
    result = classify_intent(query)
    print("\n🔁 Classification Result:", result)
