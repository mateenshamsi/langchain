from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.7,
    max_tokens=256
)

# Prompts
joke_prompt = PromptTemplate(input_variables=['topic'], template="Tell me a joke about {topic}.")
fact_prompt = PromptTemplate(input_variables=['topic'], template="Tell me a fun fact about {topic}.")

# Parser
parser = StrOutputParser()

# Runnable chains
joke_chain = joke_prompt | llm | parser

# RunnablePassthrough just passes the topic through
passthrough = RunnablePassthrough()

# Run in parallel: one branch computes a joke, the other just passes the original topic
parallel = RunnableParallel({
    "joke": joke_chain,
    "original_topic": passthrough
})

# Invoke
result = parallel.invoke({"topic": "cats"})
print(result)
