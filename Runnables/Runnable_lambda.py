from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough, RunnableParallel, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

parser = StrOutputParser()
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-001')

def word_counter(text):
    return len(text.split())


prompt = PromptTemplate(
    template='generate a joke on {topic}',
    input_variables=['topic']
)


joke_chain = RunnableSequence(prompt, model, parser)

parellel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'wordCount': RunnableLambda(word_counter)
})

final_chain = RunnableSequence(joke_chain,parellel_chain)

print(final_chain.invoke({'topic':'AI'}))
