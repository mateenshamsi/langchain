from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence
import os
# Load environment variables
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
llm_openai = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=1.0,
    max_tokens=512   
)
prompt=PromptTemplate(
    input_variables=['fact'],
    template="Tell me a joke about {fact}."
)
parser = StrOutputParser()
chain=RunnableSequence(prompt,llm_openai,parser)
print(chain.invoke({"fact":"cats"}))