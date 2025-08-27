from typing import TypedDict,Annotated,Optional
from dotenv import load_dotenv
import streamlit as st
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Define model
model = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.7,
    max_tokens=500
)

# Define structured schema
class Review(TypedDict):
    key_themes:Annotated[list[str],"Write down all the key themes discussed in review in a list"]
    summary: Annotated[str,"A brief summary of the review"]
    sentiment: Annotated[str,"Return sentiment of review either negative,positive or neutral"] 
    pros:Annotated[Optional[list[str]],"Write down all the pros inside a list"] 
    cons:Annotated[Optional[list[str]],"Write down all the cons inside a list"]
# Attach structured output schema
structured_model = model.with_structured_output(Review)

# Input text to analyze
text = """The AuroraX Smartwatch redefines convenience by combining sleek design with powerful features. Its vibrant AMOLED display makes everything from messages to workouts look stunning. The lightweight body and customizable straps ensure it feels comfortable on the wrist, whether you’re at the gym or in the office.

On the positive side, the watch boasts impressive battery life, lasting up to five days on a single charge. The fitness tracking is accurate, covering steps, heart rate, and even sleep patterns with in-depth insights. Many users praise the seamless integration with smartphones, making calls and notifications effortless.

However, some drawbacks do exist. The app ecosystem is limited, which can feel restrictive compared to other premium smartwatches. While fitness tracking is strong, GPS performance sometimes lags in real-time navigation, causing frustration during outdoor runs. Additionally, the price point may feel steep for users who only need basic functionality.

Overall, the AuroraX Smartwatch balances innovation with practicality. While it may not satisfy tech enthusiasts who rely heavily on third-party apps, it shines as a stylish and reliable daily companion. For those seeking a watch that emphasizes fitness, battery endurance, and elegance, it delivers a largely positive experience despite a few shortcomings."""

# Invoke the model with structured output
res = structured_model.invoke(f"Analyze this text:\n\n{text}")

print(res)
