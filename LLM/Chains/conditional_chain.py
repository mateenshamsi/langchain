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
prompt_market_research = PromptTemplate(
    input_variables=["product"],
    template="Identify the target audience and potential market segments for a company selling {product}."
)

prompt_slogan = PromptTemplate(
    input_variables=["product"],
    template="Create a short, witty slogan that highlights the value of {product}."
)

prompt_competitor_analysis = PromptTemplate(
    input_variables=["product"],
    template="List three key competitors for {product} and suggest how our company can differentiate."
)
# Parser
parser = StrOutputParser()

classifier_chain = prompt_market_research|llm_openai|parser
print(classifier_chain.invoke({"product": "colorful socks"}))
