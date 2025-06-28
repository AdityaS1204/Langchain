from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

parser = StrOutputParser()
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-001')

loader = PyPDFLoader('6.pdf')
docs = loader.load()

print(len(docs))
print(docs[0].page_content)
print(docs[1].metadata)