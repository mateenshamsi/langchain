from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableBranch, RunnableSequence
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Initialize the model
model = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.7,
    max_tokens=256
)

# Define different prompts for different branches
prompt_technical = PromptTemplate(
    template='Provide a technical explanation about: {topic}',
    input_variables=['topic']
)

prompt_simple = PromptTemplate(
    template='Explain in simple terms for a 5-year-old: {topic}',
    input_variables=['topic']
)

prompt_summary = PromptTemplate(
    template='Summarize the following topic in 2-3 sentences: {topic}',
    input_variables=['topic']
)

# Parser
parser = StrOutputParser()

# Create chains for each branch
technical_chain = RunnableSequence(prompt_technical, model, parser)
simple_chain = RunnableSequence(prompt_simple, model, parser)
summary_chain = RunnableSequence(prompt_summary, model, parser)

# Define a function to determine which branch to take
def route_based_on_topic(inputs):
    """Route to different chains based on the topic content"""
    topic = inputs.get('topic', '').lower()
    
    # Route based on keywords in the topic
    if any(word in topic for word in ['technical', 'code', 'algorithm', 'programming']):
        return technical_chain
    elif any(word in topic for word in ['simple', 'easy', 'basic', 'child']):
        return simple_chain
    else:
        return summary_chain

# Create the RunnableBranch with conditions
branch_chain = RunnableBranch(
    # First condition: check if topic contains "technical" keywords
    (
        lambda x: any(word in x.get('topic', '').lower() for word in ['technical', 'code', 'algorithm', 'programming']),
        technical_chain
    ),
    # Second condition: check if topic contains "simple" keywords
    (
        lambda x: any(word in x.get('topic', '').lower() for word in ['simple', 'easy', 'basic', 'child']),
        simple_chain
    ),
    # Default branch (fallback)
    summary_chain
)

# Example usage
if __name__ == "__main__":
    # Test different topics to see branching in action
    test_topics = [
        {"topic": "Explain the technical details of machine learning"},
        {"topic": "Tell me in simple terms what is artificial intelligence"},
        {"topic": "Climate change and its effects on the environment"}
    ]
    
    print("=" * 60)
    print("Testing RunnableBranch with different topics:")
    print("=" * 60)
    
    for test_input in test_topics:
        print(f"\nTopic: {test_input['topic']}")
        print("-" * 40)
        result = branch_chain.invoke(test_input)
        print(f"Response: {result}")
        print("-" * 40)