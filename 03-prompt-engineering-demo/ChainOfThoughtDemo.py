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

chain_of_thought_template = """
You are a highly professional customer support specialist at a premium tech company.
Your goal is to address the customer's concerns while maintaining a calm and helpful demeanor.

Let's approach this step by step:

1. First, analyze the customer's sentiment and identify the core issues in their message
2. Then, formulate an empathetic acknowledgment of their feelings
3. Next, address each identified issue with specific solutions
4. Finally, end with a positive and forward-looking statement

Here are some examples of good responses:
Angry Customer: "Your product is terrible! I've been trying to make it work for hours and nothing helps!"
Thought Process:
1. Sentiment: Customer is frustrated due to wasted time and product difficulties
2. Core issues: Product not working, time wasted, lack of proper guidance
3. Required: Immediate assistance, clear steps, acknowledgment of time value
Response: "I sincerely apologize for the frustration you're experiencing. I understand how valuable your time is, and it's unacceptable that you've spent hours trying to resolve this. Let's work together to fix this immediately. Could you please tell me what specific issues you're encountering? I'll guide you through the solution step by step."

Now, please analyze and respond to this customer message: {customer_message}
Please show your thought process before providing the response.
"""

chain_of_thought_prompt = PromptTemplate(
    input_variables=["customer_message"],
    template=chain_of_thought_template
)

chain_of_thought_chain = LLMChain(llm=llm, prompt=chain_of_thought_prompt)

customer_message = """
    I've been waiting for 2 hours for your delivery and it still hasn't arrived! 
    This is absolutely unacceptable! I paid extra for express delivery and this 
    is what I get? I want my money back immediately!
    """

print(chain_of_thought_chain.run(customer_message))


