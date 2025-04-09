from langchain_pinecone import PineconeVectorStore
from chunker import vector_store
# Define retriever function to get relevant chunks
def retrieve_context(query):
    similar_chunks = vector_store.similarity_search(query, k=10)
    # Combine the content of the chunks into a single context string
    return "\n\n".join([chunk.page_content for chunk in similar_chunks])