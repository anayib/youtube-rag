import os
from pinecone import Pinecone, ServerlessSpec
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Pinecone
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
cloud = os.getenv('PINECONE_CLOUD', 'aws')  # Default to AWS if not set
region = os.getenv('PINECONE_REGION', 'us-east-1')  # Default to us-east-1 if not set
spec = ServerlessSpec(cloud=cloud, region=region)
index_name = "transcription-index"

# Load and chunk the transcription file
loader = TextLoader("transcription.txt")
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(documents)

# Initialize embeddings model
embeddings_model = OllamaEmbeddings(model="llama3.2")

# Create or connect to Pinecone index and initialize vector store
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=3072,
        metric='cosine',
        spec=spec
    )

# Initialize vector store with the embeddings model
def get_vector_store():
    stats = pc.Index(index_name).describe_index_stats()
    if stats['total_vector_count'] == 0:
        return PineconeVectorStore.from_documents(
            documents=chunks,
            embedding=embeddings_model,
            index_name=index_name
        )
    else:
        print("Vectors already exist, using existing index")
        return PineconeVectorStore.from_existing_index(index_name, embeddings_model)

vector_store = get_vector_store()