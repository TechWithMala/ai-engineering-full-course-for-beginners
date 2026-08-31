# pip install langchain-openai

from langchain_openai import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate, 
    HumanMessagePromptTemplate,
)
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read the key
api_key = os.getenv('API_KEY')

os.environ["OPENAI_API_KEY"] = api_key

# Create a simple prompt by using HumanMessagePromptTemplate  
human_message_prompt = HumanMessagePromptTemplate.from_template(
    "Make up a funny company name for a company that produces {product}"
)

# Chat prompt template
chat_prompt_template = ChatPromptTemplate.from_messages([human_message_prompt])

# Initiaize LLM
llm = ChatOpenAI()

# bind LLM and chat prompt template
chain = chat_prompt_template | llm

# print(llm)

topic = "Dance"
funnyCompanyName = chain.invoke(input=topic).content

# print(funnyCompanyName)

print("\n\033[1m Make up a funny company name for the topic " + topic)
print("-" * 50)
print('\033[0m' + funnyCompanyName)
