from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


def build_qa_chain(chunks):

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004")
    vectoreStore = FAISS(chunks, embeddings)
    retriever = vectoreStore.as_retriever(
        search_type='similarity', kwargs={'k': 4})
    prompt = PromptTemplate(
        template="""
         you are a helpful assistant.
    Answer form the provided transcript context.
    if the context is insufficient, just say you don't know.
    {context}
    Question: {question}
         """,
        input_variables=['context', 'question']
    )

    def format_text(retrieved_docs):
        return '\n\n'.join(doc.page_content for doc in retrieved_docs)

    context_chain = RunnableParallel({
        'context': retriever | RunnableLambda(format_text),
        'question':RunnablePassthrough()
    })
    
    model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-001')
    parser = StrOutputParser()
    
    return context_chain | prompt | model | parser
    
