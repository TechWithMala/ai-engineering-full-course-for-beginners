#pip install langchain_anthropic

from langchain_anthropic import ChatAnthropic
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory
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
memory = ConversationBufferWindowMemory( k=1, return_messages=True)

memory.save_context({"input": "hi"}, {"output": "whats up"})
memory.save_context({"input": "not much you"}, {"output": "not much"})
memory.load_memory_variables({})

memory= ConversationBufferWindowMemory(k=1)

conversation=ConversationChain(memory=memory, 
                  llm=llm,
                  verbose=True)

print(conversation.predict(input="Hi, this is Mala?"))
print(conversation.predict(input="2*2 is 4"))
print(conversation.predict(input="what is my name"))

