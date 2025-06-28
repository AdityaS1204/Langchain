from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

parser = StrOutputParser()
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-001')
prompt = PromptTemplate(
    template='summarize the poem:\n {text}',
    input_variables=['text']
)

loader = TextLoader('cricket.txt', encoding='UTF-8')
docs = loader.load()
chain = prompt | model | parser

print(chain.invoke({'text':docs[0].page_content}))
