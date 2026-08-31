# pip install langchain-openai

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read the key
api_key = os.getenv('API_KEY')

os.environ["OPENAI_API_KEY"] = api_key

# Initiaize LLM
llm = ChatOpenAI()

# Define prompt template
template = "Give me a simple bullet point outline for a blog post on {topic}"

topic = "AI"

# Create prompt
first_prompt = ChatPromptTemplate.from_template(template)

# Create chain one
chain_one = first_prompt|llm

# print('CHAIN ONE ==========>',  chain_one)
chain_one_result = chain_one.invoke(topic)

print("\n\033[1m Give me a simple bullet point outline for a blog post")
print("-" * 50)
print('\033[0m' + chain_one_result.content)

# Define prompt template
template = "Write a blog post using this outline: {abc}"

# Create prompt
second_prompt = ChatPromptTemplate.from_template(template)

# Create chain two
chain_two = second_prompt|llm

# print('CHAIN TWO ==========>',  chain_two)

full_chain = chain_one|chain_two

result = full_chain.invoke(topic)

print("\n\033[1m Write a blog post using the outline")
print("-" * 50)
print('\033[0m' + result.content)

