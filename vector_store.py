from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Sample documents
documents = [
    "LangChain helps build AI applications.",
    "Vector databases store embeddings.",
    "Agents can use tools dynamically."
]

# Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create vector store
vectorstore = FAISS.from_texts(
    documents,
    embedding=embeddings
)

# Similarity search
results = vectorstore.similarity_search(
    "What are embeddings?"
)

print("\nSearch Results:\n")

for result in results:
    print(result.page_content)