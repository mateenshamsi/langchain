import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser 
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)
strParser = StrOutputParser() 
model = ChatHuggingFace(llm=llm)

# First prompt
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

# Second prompt
template2 = PromptTemplate(
    template="Write a 5 line summary on {text}",
    input_variables=["text"]
)

chain = template1|model|strParser|template2|model|strParser  

result=chain.invoke({'topic':'black hole'}) 
print(result)
