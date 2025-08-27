from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableSequence
import os
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
llm_openai = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=1.0,
    max_tokens=512   
)
prompt1=PromptTemplate(
    input_variables=['topic'],
    template="Tell me a joke about {topic}."
)
prompt2=PromptTemplate(
    input_variables=['topic'],
    template="Tell me a fun fact about {topic}."
)
parser = StrOutputParser()
chain=RunnableParallel({
    'tweet':RunnableSequence(prompt1,llm_openai,parser),
    'fact':RunnableSequence(prompt2,llm_openai,parser) 
})
print(chain.invoke({"topic":"dogs"}))