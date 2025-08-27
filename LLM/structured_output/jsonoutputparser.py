import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser 

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model = ChatHuggingFace(llm=llm)

# JSON parser
parser = JsonOutputParser()

# Prompt with format instructions
template1 = PromptTemplate(
    template=(
        "Give me the name, age, and city of a fictional character.\n"
        "Return only valid JSON. Do not include explanations, comments, or extra text.\n"
        "{format_type}"
    ),
    input_variables=[],
    partial_variables={'format_type': parser.get_format_instructions()}
)

  
chain=template1|model|parser 
res=chain.invoke({})
print("\n=== Parsed JSON ===\n", res)
