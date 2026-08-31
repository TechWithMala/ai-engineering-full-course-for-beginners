# pip install langchain-openai

from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
from sqlalchemy import MetaData
from sqlalchemy import Column, Integer, String, Table, Date, Float
from sqlalchemy import create_engine
from sqlalchemy import insert
from datetime import datetime
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read the API keys
openai_api_key = os.getenv('OPENAI_API_KEY')

os.environ["OPENAI_API_KEY"] = openai_api_key

# Initialize OpenAI LLM
llm = OpenAI(temperature=0)

def count_tokens(agent, query):
    with get_openai_callback() as cb:
        result = agent(query)
        print(f'Spent a total of {cb.total_tokens} tokens')


    return result

metadata_obj = MetaData()

stocks = Table(
    "stocks",
    metadata_obj,
    Column("obs_id", Integer, primary_key=True),
    Column("stock_ticker", String(4), nullable=False),
    Column("price", Float, nullable=False),
    Column("date", Date, nullable=False),
)

engine = create_engine("sqlite:///:memory:")
metadata_obj.create_all(engine)

observations = [
    [1, 'ABC', 200, datetime(2050, 1, 1)],
    [2, 'ABC', 208, datetime(2050, 1, 2)],
    [3, 'ABC', 232, datetime(2050, 1, 3)],
    [4, 'ABC', 225, datetime(2050, 1, 4)],
    [5, 'ABC', 226, datetime(2050, 1, 5)],
    [6, 'XYZ', 810, datetime(2050, 1, 1)],
    [7, 'XYZ', 803, datetime(2050, 1, 2)],
    [8, 'XYZ', 798, datetime(2050, 1, 3)],
    [9, 'XYZ', 795, datetime(2050, 1, 4)],
    [10, 'XYZ', 791, datetime(2050, 1, 5)],
]

def insert_obs(obs):
    stmt = insert(stocks).values(
    obs_id=obs[0],
    stock_ticker=obs[1],
    price=obs[2],
    date=obs[3]
    )

    with engine.begin() as conn:
        conn.execute(stmt)

for obs in observations:
    insert_obs(obs)

db = SQLDatabase(engine)

sql_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)

agent_executor = create_sql_agent(
    llm=llm,
    toolkit=SQLDatabaseToolkit(db=db, llm=llm),
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    max_iterations=30
)

result = count_tokens(
    agent_executor,
    "What is the multiplication of the ratio between stock " +
    "prices for 'ABC' and 'XYZ' in January 3rd and the ratio " +
    "between the same stock prices on January the 4th?"
)

print(result)

