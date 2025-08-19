from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv 
import os
load_dotenv() 
OPENROUTER_API_KEY=os.getenv("OPENROUTER_API_KEY")
llm = ChatOpenAI(
    model="gpt-4o-mini",                         # OpenRouter model
    openai_api_key=OPENROUTER_API_KEY,           # key from .env
    openai_api_base="https://openrouter.ai/api/v1",  # OpenRouter endpoint
    temperature=1.5
) 
result=llm.invoke("Tell me a joke based on chatgpt") 
print(result)