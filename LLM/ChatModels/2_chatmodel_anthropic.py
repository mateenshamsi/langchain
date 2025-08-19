from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

llm = ChatOpenAI(
    model="anthropic/claude-3.5-sonnet",
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.7,
    max_tokens=500  # Limit output length
)

result = llm.invoke("Tell me a joke about ChatGPT and AI assistants in hinglish")
print(result.content)

