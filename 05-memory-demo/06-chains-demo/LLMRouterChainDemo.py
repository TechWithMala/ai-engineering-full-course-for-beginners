# pip install langchain-openai

from langchain_openai import ChatOpenAI
from langchain.chains.router import MultiPromptChain
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read the key
api_key = os.getenv('API_KEY')

os.environ["OPENAI_API_KEY"] =api_key

# Initialize LLM
llm = ChatOpenAI()

# Route templates
beginner_template = '''You are a physics teacher who is really
focused on beginners and explaining complex topics in simple to understand terms.
You assume no prior knowledge. Here is the question\n{input}'''

expert_template = '''You are a world expert physics professor who explains physics topics
to advanced audience members. You can assume anyone you answer has a
PhD level understanding of Physics. Here is the question\n{input}'''

empty_template = 'empty'

# Route prompts
prompt_infos = [
    {'name':'empty','description':'Replies to empty questions','prompt_template':empty_template},
    {'name':'advanced physics','description': 'Answers advanced physics questions',
     'prompt_template':expert_template},
    {'name':'beginner physics','description': 'Answers basic beginner physics questions',
     'prompt_template':beginner_template},
   
]

# Routing Chain Call
chain = MultiPromptChain.from_prompts(llm, prompt_infos, verbose=True)

print(chain.invoke("How do magnets work explain?"))
print(chain.invoke("How do Feynman Diagrams work?"))