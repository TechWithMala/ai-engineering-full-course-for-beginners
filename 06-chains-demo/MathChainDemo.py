# pip install langchain-openai
# pip install numexpr

from langchain_openai import ChatOpenAI
from langchain.chains import LLMMathChain
from langchain.schema import (
    HumanMessage
    )

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read the key
api_key = os.getenv('API_KEY')

os.environ["OPENAI_API_KEY"] =api_key

# Initialize LLM
llm = ChatOpenAI()

result = llm.invoke([HumanMessage(content="What is 17 raised to the power of 11?")])

print("\n\033[1m What is 17 raised to the power of 11?")
print("-" * 50)
print('\033[0m' + result.content)

result = llm.invoke([HumanMessage(content="Give me the Python formula that represents: What is 17 raised to the power of 11? Only reply with the formula, nothing else!")])

print("\n\033[1m Give me the Python formula that represents: What is 17 raised to the power of 11? Only reply with the formula, nothing else!")
print("-" * 50)
print('\033[0m' + result.content)

llm_math_model = LLMMathChain.from_llm(llm)
print("\n\033[1m What is 17 raised to the power of 11?")
print("-" * 50)
print('\033[0m')
print(llm_math_model.invoke("What is 17 raised to the power of 11?"))

