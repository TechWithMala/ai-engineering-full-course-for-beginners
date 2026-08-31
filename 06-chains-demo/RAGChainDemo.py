# pip install langchain-openai
# pip install chromadb

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read the key
api_key = os.getenv('API_KEY')

os.environ["OPENAI_API_KEY"] =api_key

# Initialize LLM
llm = ChatOpenAI()

# Define input document
documents=[
    "HP printer sales are up by 30% in 2011 Q4",
    "Lenovo Laptop sales are down by 10% in 2012",
    "A3 printer sales is 5% more in middle east as compared to A4 total"
]

# Create text splitter and split the input document
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)

splits =  text_splitter.create_documents(documents)

print(f"Document has been split into {len(splits)} chunks.")
print("\n\033[1mExample chunks:")
print("-" * 50)
print('\033[0m')
for i, chunk in enumerate(splits):
    print(f"\nChunk {i+1}:")
    print(chunk)
    print("-" * 30)

# Define embeddings
embeddings = OpenAIEmbeddings()

# create vector store using the initialized embeddings model
vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)

# create retriever
retriever = vectorstore.as_retriever()

# Create a RAG template
template = """Answer the following question based on the provided context:
            Context: {context}
            Question: {question}


            Answer:"""

# Create a RAG prompt
prompt = ChatPromptTemplate.from_template(template)

# Create RAG chain
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

question = "What is Apple printer sales in 2011 Q4?"
answer = rag_chain.invoke(question)
print(f"\033[1m Question: {question}")
print(f"\033[0m Answer: {answer}")
