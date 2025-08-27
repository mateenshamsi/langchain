from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

import os

# Load environment variables
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Define LLMs
llm_openai = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=1.0,
    max_tokens=512   # 👈 stay well under your free quota
)

llm_claude = ChatOpenAI(
    model="anthropic/claude-3.5-sonnet",
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=1.0,
    max_tokens=512   # 👈 same here
)

# Prompts
prompt_name = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?"
)

prompt_tagline = PromptTemplate(
    input_variables=["product"],
    template="Suggest a catchy tagline for a company that makes {product}."
)

prompt_usp = PromptTemplate(
    input_variables=["product"],
    template="List three unique selling points for a company that makes {product}."
)

# Parser
parser = StrOutputParser()

# Parallel execution: run both prompts at once
parallel_chain = RunnableParallel(
    name = prompt_name | llm_openai | parser,
    tagline = prompt_tagline | llm_claude | parser,
)

# Final merged chain (takes output of parallel + product → generates USP)
final_chain = {
    "ideas": parallel_chain,
    "usp": prompt_usp | llm_openai | parser
}

# Invoke
result = RunnableParallel(**final_chain).invoke({"product": "colorful socks"})
print(result)
