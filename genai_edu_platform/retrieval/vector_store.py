import faiss
import numpy as np

stored_chunks = []
stored_vectors = None

def store_embeddings(chunks, embeddings):
    global stored_chunks, stored_vectors
    stored_chunks = chunks
    stored_vectors = np.array(embeddings).astype("float32")
    index = faiss.IndexFlatL2(len(stored_vectors[0]))
    index.add(stored_vectors)
    globals()["index"] = index

def search_similar(query_embedding, top_k=3):
    D, I = globals()["index"].search(np.array([query_embedding]).astype("float32"), top_k)
    return [stored_chunks[i] for i in I[0]]