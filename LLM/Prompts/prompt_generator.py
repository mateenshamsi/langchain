from langchain_core.prompts import PromptTemplate
# Prompt template
template = """
You are an expert research summarizer.

Summarize the paper "{paper}" in a {style} style. 
The summary should be limited to {length} words.

Guidelines:
- If the paper contains mathematical models or equations, include them where relevant.
- If it helps with understanding, use analogies or intuitive examples.
- Maintain clarity, accuracy, and relevance.
- Adapt tone and explanation depth based on the selected style.

User instructions: {user_input}
"""

prompt_template = PromptTemplate(
    input_variables=["paper", "style", "length", "user_input"],
    template=template,
)

prompt_template.save('template.json') 