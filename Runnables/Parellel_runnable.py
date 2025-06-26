from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.runnable import RunnableSequence,RunnableParallel
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a tweeter post on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a Linkedin post on {topic}',
    input_variables=['topic']
)


model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-001')
parser = StrOutputParser()

parellel_chain = RunnableParallel({
    'tweet':RunnableSequence(prompt1,model,parser),
    'linkendin':RunnableSequence(prompt2,model,parser)
})

print(parellel_chain.invoke({'topic':'AI'}))