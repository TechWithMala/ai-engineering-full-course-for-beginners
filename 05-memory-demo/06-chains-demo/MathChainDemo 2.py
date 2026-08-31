# pip install langchain-openai
# pip install numexpr

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMMathChain
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read the key
api_key = os.getenv('API_KEY')

os.environ["OPENAI_API_KEY"] =api_key

# Initialize LLM
llm = ChatOpenAI()

# define math prompt
math_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a mathematical assistant that helps solve math problems.
        Given a math problem, respond with ONLY a Python expression that can be evaluated to solve it.
        You must start your response with 'Answer: ' followed by the expression.
        Do not include any other text or explanations.

        For example:
        Question: What is 2 plus 2?
        Answer: 2 + 2

        Question: If I have 3 apples and multiply them by 4, how many do I have?
        Answer: 3 * 4

        Question: What is 25 times 4?
        Answer: 25 * 4"""),
        ("user", "{question}")
])

math_chain = LLMMathChain.from_llm(llm=llm, prompt=math_prompt)

math_question = "What is 100 times 4?"
math_result = math_chain.invoke({"question": math_question})
print(f"Question: {math_question}")
print(f"Answer: {math_result['answer']}")

