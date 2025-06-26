from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.runnable import RunnableSequence,RunnablePassthrough,RunnableParallel
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template='write a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='explain tthis joke: {text}',
    input_variables=['text']
)


model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-001')
parser = StrOutputParser()

joke_chain = RunnableSequence(prompt,model,parser)
chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'explaination':RunnableSequence(prompt2,model,parser)
})

final_chain = RunnableSequence(joke_chain,chain)

print(final_chain.invoke({'topic':'AI'}))