# pip install langchain-openai

from langchain.chains import LLMMathChain
from langchain.agents import Tool
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read the API keys
openai_api_key = os.getenv('OPENAI_API_KEY')

os.environ["OPENAI_API_KEY"] = openai_api_key

# Initialize LLM
llm = OpenAI(temperature=0.8)

# Initialize LLMMathChain
llm_math = LLMMathChain(llm=llm)

# initialize the math tool
math_tool = Tool(
    name='Calculator',
    func=llm_math.run,
    description='Useful for when you need to answer questions about math.'
)

tools = [math_tool]

tools = load_tools(
    ['llm-math'],
    llm=llm
)

zero_shot_agent = initialize_agent(
    agent="zero-shot-react-description",
    tools=tools,
    llm=llm,
    verbose=True,
    max_iterations=3
)

print(zero_shot_agent("what is (4.5*2.1)^2.2?"))

# print((4.5*2.1)**2.2)

zero_shot_agent("if Mary has four apples and Tom brings two and a half apple "
                "boxes (apple box contains eight apples), how many apples do we "
                "have?")

# zero_shot_agent("what is the capital of the United States of America?")

# Initialize prompt template 
prompt = PromptTemplate(
    input_variables=["query"],
    template="{query}"
)

llm_chain = LLMChain(llm=llm, prompt=prompt)

llm_tool = Tool(
    name='Language Model',
    func=llm_chain.run,
    description='use this tool for general purpose queries and logic'
)

tools.append(llm_tool)

zero_shot_agent = initialize_agent(
    agent="zero-shot-react-description",
    tools=tools,
    llm=llm,
    verbose=True,
    max_iterations=3
)

zero_shot_agent("what is the capital of the United States of America?")
zero_shot_agent("what is (4.5*2.1)^2.2?")