from langchain.embeddings import OpenAIEmbeddings
from retrieval.vector_store import store_embeddings

def embed_chunks(chunks):
    embedder = OpenAIEmbeddings(model="text-embedding-ada-002", deployment="your-azure-deployment")
    embeddings = embedder.embed_documents(chunks)
    store_embeddings(chunks, embeddings)