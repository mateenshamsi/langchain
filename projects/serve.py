from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq 
import os 
from langserve import add_routes
from dotenv import load_dotenv
from langserve.validation import chainBatchRequest
load_dotenv()

chainBatchRequest.model_rebuild()

groq_api_key = os.getenv("GROQ_API_KEY") 
model=ChatGroq(model="Gemma2-9b-It",groq_api_key=groq_api_key) 


# 1.Creating prompt template 
from langchain_core.prompts import ChatPromptTemplate 
generic_template="Translate the following into {language}:"
prompt=ChatPromptTemplate.from_messages(
    [
        ("system",generic_template),
        ("user","{text}") 

    ]
) 
result=prompt.invoke({"language":"French","text":"Hello"})
result.to_messages()

parser=StrOutputParser()
chain = prompt|model|parser
# App Definition 
app=FastAPI(title="Langchainserver",version="1.0",description="A simple API server using runnable interfaces") 

add_routes(
    app,
    chain,
    path="/chain" 

)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="localhost",port=8000)