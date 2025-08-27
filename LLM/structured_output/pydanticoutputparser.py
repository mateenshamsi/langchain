from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
import os
from pydantic import BaseModel, Field

load_dotenv()

# LLM setup
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)
model = ChatHuggingFace(llm=llm)

# Define schema
class Student(BaseModel):
    name: str = Field(description="Name of person")
    age: int = Field(gt=18, description="Age of person (must be > 18)")
    city: str = Field(description="Name of city")

# Parser
parser = PydanticOutputParser(pydantic_object=Student)

# Prompt
template = PromptTemplate(
    template="Generate the name, age, and city of a fictional person.\n{format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()},
)

# Chain: Prompt -> Model -> Parser
chain = template | model | parser

# Run
res = chain.invoke({})
print("\n=== Parsed Pydantic Object ===\n", res)
print("\nName:", res.name)
print("Age:", res.age)
print("City:", res.city)
