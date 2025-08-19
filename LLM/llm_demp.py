from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY not found in environment variables")

# Initialize ChatOpenAI with OpenRouter endpoint
llm = ChatOpenAI(
    model="gpt-4o-mini",                         # OpenRouter model
    openai_api_key=OPENROUTER_API_KEY,           # key from .env
    openai_api_base="https://openrouter.ai/api/v1",  # OpenRouter endpoint
    temperature=0
)

# Send a message using invoke()
response = llm.invoke([HumanMessage(content="What is the capital of India?")])
print(response.content)
