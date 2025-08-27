from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
import os

load_dotenv()

# LLM
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)
model = ChatHuggingFace(llm=llm)

# Schema for structured output
schema = [
    ResponseSchema(name="Fact1", description="Fact 1 about the topic"),
    ResponseSchema(name="Fact2", description="Fact 2 about the topic"),
    ResponseSchema(name="Fact3", description="Fact 3 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

# Prompt with format instructions
template = PromptTemplate(
    template="Give 3 facts about {topic}\n{format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)

# Chain
chain = template | model | parser

# Run
res = chain.invoke({"topic": "black hole"})
print("\n=== Parsed JSON ===\n", res)
print("\nFact 1:", res["Fact1"])
print("Fact 2:", res["Fact2"])
print("Fact 3:", res["Fact3"])
