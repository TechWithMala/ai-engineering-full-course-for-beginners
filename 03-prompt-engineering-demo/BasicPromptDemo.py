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

# Define prompt template
basic_template = """
Reply to this customer message: {customer_message}
"""

basic_prompt = PromptTemplate(
    input_variables=["customer_message"],
    template=basic_template
)

basic_chain = LLMChain(llm=llm, prompt=basic_prompt)

customer_message = """
    I've been waiting for 2 hours for your delivery and it still hasn't arrived! 
    This is absolutely unacceptable! I paid extra for express delivery and this 
    is what I get? I want my money back immediately!
    """

print(basic_chain.run(customer_message))

