from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from grandalf.graphs import Edge, Graph, Vertex
from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate(
    template='Genrate 5 intersting facts about {topic}',
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-001')
parser = StrOutputParser()

chain = prompt | model | parser 

result = chain.invoke({'topic':'nagpur'})
print(result)

chain.get_graph().print_ascii()