import faiss
import pickle
import numpy as np
import os
from sentence_transformers import SentenceTransformer

# Load model and index once
model = SentenceTransformer("all-MiniLM-L6-v2")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FAISS_INDEX_PATH = os.path.join(BASE_DIR, "vector_db", "vector.index")
METADATA_PATH = os.path.join(BASE_DIR, "vector_db", "metadata.pkl")

with open(METADATA_PATH, "rb") as f:
    metadata = pickle.load(f)
index = faiss.read_index(FAISS_INDEX_PATH)

def retrieve_chunks(query: str, top_k: int = 5) -> list:
    """
    Retrieve top-k most relevant chunks from the FAISS index for a given query.
    Returns a list of {text: ..., source: ..., page: ...} dicts.
    """
    print('*'*10)
    print('GETTING CHUNKS')
    print('*'*10)
    if not query:
        return []

    query_vector = model.encode([query])
    distances, indices = index.search(np.array(query_vector).astype("float32"), top_k)

    results = []
    for idx in indices[0]:
        if 0 <= idx < len(metadata):
            results.append(metadata[idx])

    return results

#FOR TESTING
if __name__ == "__main__":
    results = retrieve_chunks("what is a vision transformer?")
    print(results)
    print(results[0])

"""
results is a list[dict,dict]
each entry in results contains a dictionary
the dictionary looks like
{
    content: str
    source_file: str
    page: int
}
"""