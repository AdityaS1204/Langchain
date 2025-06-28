from langchain_community.document_loaders import WebBaseLoader
from bs4 import BeautifulSoup



loader = WebBaseLoader(web_path='https://www.amazon.in/Apple-MacBook-Laptop-14%E2%80%91core-20%E2%80%91core/dp/B0DLJ5313D')

docs = loader.load()

print(docs[0].page_content)
print(docs[0].metadata)