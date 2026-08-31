# pip install langchain-openai

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from operator import itemgetter

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read the key
api_key = os.getenv('API_KEY')

os.environ["OPENAI_API_KEY"] =api_key

# Initialize LLM
llm = ChatOpenAI()

# Define prompt
topic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant who generates interesting topics."),
    ("user", "Generate a random academic topic for discussion.")
])

# Create topic chain
topic_chain = topic_prompt | llm | StrOutputParser()

# second chain to generate questions about the topic..
# Define prompt
question_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant who generates thought-provoking topics."),
    ("user", "Generate 3 thought-provoking questions about this topic: {topic}.")
])

# Create question chain
question_chain = question_prompt | llm | StrOutputParser()

# Create sequential chain 
sequential_chain = {"topic": topic_chain} | RunnablePassthrough() | {
                        "topic": itemgetter("topic"),
                        "questions": question_chain
                    }

results = sequential_chain.invoke({})

# And, print the results
print("\n\033[1m Generate 3 thought-provoking questions about a random academic topic")
print("-" * 50)
print('\033[0m' + results['questions'])



