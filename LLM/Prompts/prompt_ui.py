from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st 
import os
from langchain_core.prompts import PromptTemplate,load_prompt
# Load environment variables
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Initialize LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.7,
    max_tokens=500
)

# Streamlit UI
st.set_page_config(page_title="AI Paper Summarizer", layout="centered")
st.title("📄 AI Paper Summarizer")
st.markdown("Summarize top research papers in your preferred **style** and **length**.")

# Sidebar settings
with st.sidebar:
    st.header("⚙️ Settings")

    paper_options = [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-4 Technical Report",
        "Stable Diffusion: High-Resolution Image Synthesis",
        "AlphaFold: Protein Structure Prediction"
    ]
    selected_paper = st.selectbox("📑 Select a paper", paper_options)

    style_options = [
        "Concise (bullet points)",
        "Detailed (paragraphs)",
        "Layman (easy to understand)",
        "Technical (for experts)",
        "Creative (story-like)"
    ]
    selected_style = st.selectbox("🎨 Select style", style_options)

    length_options = [
        "Short (50 words)",
        "Medium (150 words)",
        "Long (300 words)"
    ]
    selected_length = st.selectbox("📏 Select length", length_options)

    user_input = st.text_area("✍️ Add extra instructions (optional)", "")
prompt_template=load_prompt('template.json')
# Main section
if st.button("✨ Generate Summary"):
    with st.spinner("Summarizing..."):
        # Format prompt from template
        prompt = prompt_template.format(
            paper=selected_paper,
            style=selected_style.lower(),
            length=selected_length.split()[1],  # Extract number
            user_input=user_input
        )

        # Call LLM
        result = llm.invoke(prompt)

        st.subheader(f"📌 Summary of '{selected_paper}'")
        st.write(result.content)

        # Download button
        st.download_button(
            "⬇️ Download Summary",
            result.content,
            file_name=f"{selected_paper.replace(' ', '_')}_summary.txt"
        )
