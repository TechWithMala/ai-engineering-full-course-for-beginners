# pip install langchain-community
# pip install openai

import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

# Load environment variables from .env file
load_dotenv()

# Read the key
api_key = os.getenv('API_KEY')

os.environ["OPENAI_API_KEY"] =api_key

# Initialize the LLM
llm = ChatOpenAI(temperature=0.7)


constrained_template = """
You are a customer support specialist. Generate a response to the customer's message following these strict constraints:

1. Response must be exactly 3 paragraphs long
2. First paragraph must be exactly 2 sentences showing empathy
3. Second paragraph must provide exactly 2 concrete solutions
4. Third paragraph must end with a question to engage the customer
5. Total response must maintain a professional tone
6. Must not use any exclamation marks
7. Must include exactly one apology
8. Must use the phrase "I understand" exactly once

Customer message: {customer_message}
"""

constrained_prompt = PromptTemplate(
    input_variables=["customer_message"],
    template=constrained_template
)

constrained_chain = LLMChain(llm=llm, prompt=constrained_prompt)

customer_message = """
    I've been waiting for 2 hours for your delivery and it still hasn't arrived! 
    This is absolutely unacceptable! I paid extra for express delivery and this 
    is what I get? I want my money back immediately!
    """

print(constrained_chain.run(customer_message))



