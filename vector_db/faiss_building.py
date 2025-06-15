import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer
from chunking import get_all_pdf_chunks 

chunks_with_metadata = get_all_pdf_chunks()

texts = [chunk["content"] for chunk in chunks_with_metadata]


model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)

dimension = embeddings.shape[1]
# index = faiss.IndexFlatL2(dimension)  
# index.add(embeddings)
index = faiss.IndexFlatIP(dimension)
embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
index.add(embeddings)


faiss.write_index(index, "vector.index")

with open("metadata.pkl", "wb") as f:
    pickle.dump(chunks_with_metadata, f)

print("✅ FAISS index and metadata saved.")

'''
Each entry in metadata.pkl looks like:
{
    'content':     'Learning Transferable Visual Models From Natural Language Supervision\nAlec Radford* 
                    1Jong Wook Kim* 1Chris Hallacy1Aditya Ramesh1Gabriel Goh1Sandhini Agarwal1\nGirish Sastry1Amanda Askell1Pamela Mishkin1Jack Clark1Gretchen 
                    Krueger1Ilya Sutskever1\nAbstract\nState-of-the-art computer vision systems are\ntrained to predict a ﬁxed set 
                    of predetermined\nobject categories. This restricted form of super-\nvis', 
    'source_file': 'CLIP.pdf', 
    'page': 1
} 
'''