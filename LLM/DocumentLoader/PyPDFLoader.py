from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader('LLM\DocumentLoader\ABDULMATEEN M SHAMSI.pdf')
docs=loader.load()
print(docs[0].page_content)
print(docs[0].metadata)