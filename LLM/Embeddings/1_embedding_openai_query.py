from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2") 

text = "Delhi is the capital of India"
documents=[
    "Delhi is the capital of India",
    "Kolkata is the capital of Bengal",
    "France is the capital of France"

]
embedding_vector = embeddings.embed_documents(documents) 

print(str(embedding_vector))