from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.runnable import RunnableSequence,RunnableBranch,RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-001')
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Generate a report on the topic:\n {topic}',
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template='Summarize the following text:\n {text}',
    input_variables=['text']
)

report_gen_chain = RunnableSequence(prompt1,model,parser)
branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)



chain = RunnableSequence(report_gen_chain,branch_chain)

print(chain.invoke({'topic':'Isreal vs Iran'}))