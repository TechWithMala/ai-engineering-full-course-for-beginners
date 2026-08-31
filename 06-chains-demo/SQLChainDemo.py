# pip install langchain-openai

from langchain_openai import ChatOpenAI
from langchain.chains import create_sql_query_chain
from langchain_community.utilities import SQLDatabase
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read the key
api_key = os.getenv('API_KEY')

os.environ["OPENAI_API_KEY"] =api_key

# Initialize LLM
llm = ChatOpenAI()

db = SQLDatabase.from_uri("sqlite:///Chinook.db")

chain = create_sql_query_chain(llm, db)

response = chain.invoke({"question": "How many employees are there?"})

print(response)