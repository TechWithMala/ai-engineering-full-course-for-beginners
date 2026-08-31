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

few_shot_template = """
You are a highly professional customer support specialist at a premium tech company.
Your goal is to address the customer's concerns while maintaining a calm and helpful demeanor.

Here are some examples of good responses to angry customers:

Angry Customer: "Your product is terrible! I've been trying to make it work for hours and nothing helps!"
Response: "I sincerely apologize for the frustration you're experiencing. I understand how valuable your time is, and it's unacceptable that you've spent hours trying to resolve this. Let's work together to fix this immediately. Could you please tell me what specific issues you're encountering? I'll guide you through the solution step by step."

Angry Customer: "I want a refund right now! This is the worst service ever!"
Response: "I completely understand your disappointment, and I want to make this right for you. I'll help you with the refund process right away. While I process this, could you share what specific aspects of our service didn't meet your expectations? This will help us improve and prevent similar issues in the future."

Now, please respond to this customer message: {customer_message}
"""

few_shot_prompt = PromptTemplate(
    input_variables=["customer_message"],
    template=few_shot_template
)

few_shot_chain = LLMChain(llm=llm, prompt=few_shot_prompt)

customer_message = """
    I've been waiting for 2 hours for your delivery and it still hasn't arrived! 
    This is absolutely unacceptable! I paid extra for express delivery and this 
    is what I get? I want my money back immediately!
    """

print(few_shot_chain.run(customer_message))


