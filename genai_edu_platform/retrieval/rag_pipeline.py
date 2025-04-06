from langchain.llms import AzureOpenAI
from langchain.embeddings import OpenAIEmbeddings
from .vector_store import search_similar

def get_answer(query):
    embedder = OpenAIEmbeddings(model="text-embedding-ada-002", deployment="your-azure-deployment")
    query_embedding = embedder.embed_query(query)
    context = "\n".join(search_similar(query_embedding))

    llm = AzureOpenAI(deployment_name="gpt-4", model_name="gpt-4")
    prompt = f"Use the following context to answer the question:\n{context}\n\nQuestion: {query}"
    return llm(prompt)