#pip install langchain_anthropic

from langchain_anthropic import ChatAnthropic
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read the key
anthropic_api_key = os.getenv('API_KEY')

os.environ["ANTHROPIC_API_KEY"] = anthropic_api_key

# Initialize the LLM
llm= ChatAnthropic(model="claude-3-5-sonnet-20240620")

# Memory to LLM
memory= ConversationBufferMemory()

conversation=ConversationChain(memory=memory, 
                  llm=llm,
                  verbose=True)

print(conversation.predict(input="Hi, my name is Mala"))

print(conversation.predict(input="I'm doing well! Just having a conversation with an AI."))

print(conversation.predict(input="what is AI?"))

print(conversation.predict(input="what is my name?"))