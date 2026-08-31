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
role_context_template = """
You are a highly professional customer support specialist at a premium tech company.
Your goal is to address the customer's concerns while maintaining a calm and helpful demeanor.

Customer Message: {customer_message}

Please provide a response that:
1. Acknowledges the customer's feelings
2. Addresses their concerns professionally
3. Offers concrete solutions
4. Ends with a positive note

"""
role_context_prompt = PromptTemplate(
    input_variables=["customer_message"],
    template=role_context_template
)

role_context_chain = LLMChain(llm=llm, prompt=role_context_prompt)

customer_message = """
    I've been waiting for 2 hours for your delivery and it still hasn't arrived! 
    This is absolutely unacceptable! I paid extra for express delivery and this 
    is what I get? I want my money back immediately!
    """

print(role_context_chain.run(customer_message))


