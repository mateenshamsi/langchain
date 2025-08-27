from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv() 
prompt1=PromptTemplate(
    input_variables=["product"],    
    template="What is a good name for a company that makes {product}?"
) 
prompt2=PromptTemplate(
    input_variables=["company_name"],
    template="Write a slogan for the company {company_name}."
)
import os
OPENROUTER_API_KEY=os.getenv("OPENROUTER_API_KEY")   
llm = ChatOpenAI(
    model="gpt-4o-mini",                         # OpenRouter model
    openai_api_key=OPENROUTER_API_KEY,           # key from .env
    openai_api_base="https://openrouter.ai/api/v1",  # OpenRouter endpoint
    temperature=1.5
) 
parser=StrOutputParser()
chain= prompt1|llm| prompt2|llm| parser
result=chain.invoke({"product": "colorful socks"})
print(result)