#pip install langchain_anthropic

from langchain_anthropic import ChatAnthropic
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryMemory
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read the key
anthropic_api_key = os.getenv('API_KEY')

os.environ["ANTHROPIC_API_KEY"] = anthropic_api_key

# Initialize the LLM
llm= ChatAnthropic(model="claude-3-5-sonnet-20240620")

# create a long string
schedule = "There is a meeting at 8am with your product team. \
You will need your powerpoint presentation prepared. \
9am-12pm have time to work on your LangChain \
project which will go quickly because Langchain is such a powerful tool. \
At Noon, lunch at the Italian resturant with a customer who is driving \
from over an hour away to meet you to understand the latest in AI. \
Be sure to bring your laptop to show the latest LLM demo."

memory= ConversationSummaryMemory(llm=llm, max_token_limit=100)

memory.save_context({"input": "Hello"}, {"output": "What's up"})

memory.save_context({"input": "Not much, just hanging"}, {"output": "Cool"})

memory.save_context({"input": "What is on the schedule today?"}, {"output": f"{schedule}"})

print(memory.load_memory_variables({}))

conversation=ConversationChain(memory=memory, 
                  llm=llm,
                  verbose=True)


print(conversation.predict(input="9am-12pm what will you do?"))

print(conversation.predict(input="what is deep learning"))

print(conversation.predict(input="what is AI"))