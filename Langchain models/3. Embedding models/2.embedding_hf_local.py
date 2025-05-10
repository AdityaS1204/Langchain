from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "delhi is the capital of india",
    "Mumbai is the capital of maharashtra",
    "bejing is the capital of china"
    ]

vector = embedding.embed_documents(documents)

print(str(vector))