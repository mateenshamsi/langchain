from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv
import os
from langchain.schema.runnable import RunnableLambda, RunnableSequence, RunnableParallel, RunnablePassthrough
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
prompt = PromptTemplate(input_variables=['topic'], template="Tell me a joke about {topic}.")
# Parser
parser = StrOutputParser()
# Runnable chains
joke_chain = prompt | llm | parser
# RunnableLambda to transform the topic
def transform_topic(inputs):
    topic = inputs['topic']
    transformed_topic = topic.upper()  # Example transformation: convert to uppercase
    return {'topic': transformed_topic}
parallel_chain=RunnableParallel({
    "joke": RunnablePassthrough(),
    "transformed_topic": RunnableLambda(transform_topic)
})
# Invoke
result = parallel_chain.invoke({"topic": "cats"})
print(result)