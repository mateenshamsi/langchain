from langchain_openai import ChatOpenAI
from dotenv import load_dotenv 
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
import os 
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
model=ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.7,
    max_tokens=500
)
chat_history=[]
chat_history.append(
    SystemMessage(content="You are helpful AI assistant")
) 
while True:
    user_input=input('You:')
    chat_history.append(HumanMessage(content=user_input))
    if user_input=='exit':
        break 
    result=model.invoke(chat_history)
    chat_history.append(result)  
    print("AI:",result.content) 
print(chat_history)