# pip install langchain-apify
# pip install -U langchain-community
# pip install apify-client

from langchain.indexes import VectorstoreIndexCreator
from langchain_apify import ApifyWrapper
from langchain_core.documents import Document
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.llms import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read the API keys
openai_api_key = os.getenv('OPENAI_API_KEY')
apify_api_token = os.getenv('APIFY_API_TOKEN')

os.environ["OPENAI_API_KEY"] = openai_api_key
os.environ["APIFY_API_TOKEN"] = apify_api_token

# Wrapper around Apify
apify = ApifyWrapper()

print("Call website content crawler ...")
loader = apify.call_actor(
    actor_id="apify/website-content-crawler",
    run_input={"startUrls": [{"url": "https://en.wikipedia.org/wiki/Generative_artificial_intelligence"}]},
    dataset_mapping_function=lambda item: Document(
        page_content=item["text"] or "", metadata={"source": item["url"]}
    ),
)

# Define OpenAI embedding model
embeddings = OpenAIEmbeddings()

print("Compute embeddings...")
# Initialize the vector index from the crawled documents
index = VectorstoreIndexCreator(embedding=embeddings).from_loaders([loader])

# Initialize OpenAI LLM
llm = OpenAI(temperature=0)

query = "What is Generative artificial intelligence?"

result = index.query_with_sources(query, llm=llm)
print(result)

print(result["answer"])
print(result["sources"])