# pip install langchain-openai

from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
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

# Define different prompts for different types of questions
science_prompt = PromptTemplate.from_template(
    "You are a scientific expert. Answer the following question: {input}"
)

history_prompt = PromptTemplate.from_template(
    "You are a historical expert. Answer the following question: {input}"
)

math_prompt = PromptTemplate.from_template(
    "You are a mathematics expert. Answer the following question: {input}"
)

# Create destination chains
science_chain = science_prompt | llm | StrOutputParser()
history_chain = history_prompt | llm | StrOutputParser()
math_chain = math_prompt | llm | StrOutputParser()

# Create router prompt
router_prompt = PromptTemplate.from_template(
    """Given a question, determine which category it belongs to: Science, History, or Math.
    Only respond with the category name.
   
    Question: {input}
    Category:"""
)

# Create router chain
router_chain = router_prompt | llm | StrOutputParser()

# Define routing logic
def route_chain(input_text):
     category = router_chain.invoke({"input": input_text}).strip().lower()
     if "science" in category:
        return science_chain
     elif "history" in category:
        return history_chain
     else:
         return math_chain


questions = [
    "What causes photosynthesis?",
    "Who was the first president of the United States?",
    "What is the square root of 100?"
]

for question in questions:
    print(f"\nQuestion: {question}")
    chain = route_chain(question)
    answer = chain.invoke({"input": question})
    print(f"Answer: {answer}")


