from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Load env variables
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Initialize model
model = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=1.0,
    max_tokens=512   
)

# Create summarization chain
prompt = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text:\n\n{text}\n\nSummary:"
)
parser = StrOutputParser()
chain = prompt | model | parser

# Load web content
url = "https://www.amazon.in/Amazon-Brand-Colored-Tealight-Unscented/dp/B07F32D5Z9/ref=s9_acsd_al_ot_cv2_0_t"
loader = WebBaseLoader(url)
docs = loader.load()


print(chain.invoke({"text": docs[0].page_content[:2000]}))  # slice to avoid input being too large
