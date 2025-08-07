import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec, CloudProvider, AwsRegion, Metric
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()

pinecone_key = os.getenv("PINECONE_API_KEY")

# Initialize Pinecone client
pc = Pinecone(api_key=pinecone_key)
index_name = "rag-chat-index"

# Create Pinecone index if not exists
if index_name not in [idx["name"] for idx in pc.list_indexes()]:
    pc.create_index(
        name=index_name,
        dimension=384,
        metric=Metric.DOTPRODUCT,
        spec=ServerlessSpec(
            cloud=CloudProvider.AWS,
            region=AwsRegion.US_EAST_1
        )
    )

index = pc.Index(index_name)
embed_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Upload to Pinecone
def ingest_to_pinecone(docs, metadatas):
    ids = [f"doc-{i}" for i in range(len(docs))]
    embeds = embed_model.embed_documents(docs)
    index.upsert(vectors=zip(ids, embeds, metadatas))

# Vectorstore for similarity search
vectorstore = PineconeVectorStore(
    index=index,
    embedding=embed_model,
    text_key="text"
)

def search_similar_docs(query: str, k: int = 3):
    return vectorstore.similarity_search(query, k=k)

def clear_index():
    index.delete(delete_all=True)
