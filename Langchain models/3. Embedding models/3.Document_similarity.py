from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

documents = [
    "Sachin Tendulkar is widely regarded as one of the greatest batsmen in the history of cricket.",
    "Virat Kohli is known for his aggressive batting style and leadership on the field.",
    "MS Dhoni, a legendary wicketkeeper-batsman, is celebrated for his calmness and strategic acumen.",
    "Ravindra Jadeja, an all-rounder, is known for his exceptional fielding and spinning abilities."
]

query = "tell me about MS Dhoni"

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
doc_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

# print(str(query_embedding))
# print(str(doc_embedding))

scores = cosine_similarity([query_embedding],doc_embedding)[0]
index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]
print(query)
print(documents[index])
print("Similarity score:",score)
