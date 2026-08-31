# pip install langchain
# pip install langchain-text-splitter
# pip install langchain-community 
# pip install langchain-anthropic 
# pip install sentence-transformers 
# pip install chromadb

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_anthropic import ChatAnthropic
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read the key
api_key = os.getenv('API_KEY')

os.environ["ANTHROPIC_API_KEY"] =api_key

# Step 1: Sample document
print("\nStep 1: Preparing our document")
print("-" * 50)

document = """
Artificial Intelligence (AI) is transforming the way we live and work. Machine learning, 
a subset of AI, enables computers to learn from data without explicit programming. 
Deep learning, a type of machine learning, uses neural networks inspired by the human brain.

Natural Language Processing (NLP) is a branch of AI that helps computers understand and 
process human language. It's used in applications like translation, chatbots, and text analysis.

Computer Vision is another important field in AI. It enables machines to understand and 
process visual information from the world, like images and videos. Applications include 
facial recognition, autonomous vehicles, and medical image analysis.

Reinforcement Learning is a type of machine learning where agents learn by interacting 
with an environment. They receive rewards for good actions and penalties for bad ones. 
This is used in game playing, robotics, and autonomous systems.
"""

print("Document loaded. Length:", len(document), "characters")
print("\nPreview of the document:")
print(document[:200], "...\n")

# Step 2: Text Chunking
print("\nStep 2: Chunking the document")
print("-" * 50)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50,
    length_function=len,
    separators=["\n\n", "\n", ". ", " "]
)

chunks = text_splitter.split_text(document)

print(f"Document has been split into {len(chunks)} chunks.")
print("\nExample chunks:")
for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}:")
    print(chunk)
    print("-" * 30)


# Step 3: Initialize Embeddings
print("\nStep 3: Creating embeddings")
print("-" * 50)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Embedding model loaded:", embeddings.model_name)
print("This model will convert text chunks into numerical vectors")

# OpenAI embeddings:
# embeddings = OpenAIEmbeddings()

# Step 4: Create and populate vector store
print("\nStep 4: Creating vector store")
print("-" * 50)

# Create vector store
vectorstore = Chroma.from_texts(
    texts=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

print("Vector store created with following details:")
print(f"- Number of texts: {len(chunks)}")
print(f"- Embedding dimension: {len(embeddings.embed_query('test'))}")
print(f"- Database location: ./chroma_db")

# Step 5: Similarity Search Example
print("\nStep 5: Testing similarity search")
print("-" * 50)

query = "What is reinforcement learning?"
results = vectorstore.similarity_search(query, k=2)

print(f"Query: {query}")
print("\nTop 2 most relevant chunks:")
for i, doc in enumerate(results):
    print(f"\nResult {i+1}:")
    print(doc.page_content)
    print("-" * 30)

# Step 6: Set up RAG with Anthropic Claude
print("\nStep 6: Setting up RAG pipeline")
print("-" * 50)

print("Using Anthropic Claude model with the provided API key")

# Initialize the LLM with Anthropic Claude
llm = ChatAnthropic(
    model="claude-3-5-sonnet-20240620",
    temperature=0.5
)

# OpenAI:
# if "OPENAI_API_KEY" in os.environ:
#     llm = OpenAI(
#         model_name="gpt-4",
#         temperature=0.5
#     )

# HuggingFace:
# if "HUGGINGFACEHUB_API_TOKEN" in os.environ:
#     llm = HuggingFaceHub(
#         repo_id="google/flan-t5-small",
#         model_kwargs={"temperature": 0.5, "max_length": 512}
#     )

# Create the RAG pipeline
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# Example questions to ask
questions = [
    "What is reinforcement learning and how does it work?",
    "What are the main applications of computer vision?",
    "How is NLP used in real-world applications?"
]

print("\nAsking questions to our RAG system:")

for question in questions:
    print("\nQuestion:", question)
    try:
        answer = qa_chain.invoke(question)
        print("Answer:", answer)
    except Exception as e:
        print("Error getting answer:", str(e))