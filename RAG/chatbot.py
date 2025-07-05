from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders.youtube import YoutubeLoader, TranscriptFormat
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableLambda, RunnablePassthrough, RunnableSequence
import streamlit as st
import re
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-001')
parser = StrOutputParser()
st.set_page_config(page_title="Youtube chatbot",layout="wide")
st.header("Chat with Youtube Videos")
col1,col2 = st.columns(2)
with col1:
    yt_video = st.text_input('Youtube Link:', placeholder='enter youtube video link')
    question = st.text_input('Your query:', placeholder="enter you question")
    language = st.selectbox('select video transcription language:',[
    "ar", "bn", "bg", "zh", "hr", "cs", "da", "nl", "en", "et",
    "fi", "fr", "de", "el", "iw", "hi", "hu", "id", "it", "ja",
    "ko", "lv", "lt", "no", "pl", "pt", "ro", "ru", "sr", "sk",
    "sl", "es", "sw", "sv", "th", "tr", "uk", "vi"
    ])


def extract_yt_video_id(url):
    regex = (
        r"(?:https?://)?(?:www\.)?(?:youtube\.com/(?:watch\?v=|embed/)|youtu\.be/)([\w\-]{11})"
    )
    match = re.search(regex, url)
    return match.group(1) if match else None

video_id = extract_yt_video_id(yt_video)

loader = YoutubeLoader(
    video_id=video_id,
    language=language,
    transcript_format=TranscriptFormat.TEXT,
    chunk_size_seconds=120
)
prompt = PromptTemplate(
    template='''
    you are a helpful assistant.
    Answer form the provided transcript context.
    if the context is insufficient, just say you don't know.
    {context}
    Question: {question}
    ''',
    input_variables=['context', 'question']
)

transcript = loader.load()
show_transcript = transcript[0].page_content
with col2:
    st.text_area("Video Transcript",value=show_transcript,height=500)
spliter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=100)
chunks = spliter.split_documents(transcript)
print('chunks length: ', len(chunks))

embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

vectorStore = FAISS.from_documents(chunks, embeddings)

retriever = vectorStore.as_retriever(
    search_type='similarity', search_kwargs={'k': 4})

def format_text(retrieved_docs):
    context = "\n\n".join(doc.page_content for doc in retrieved_docs)
    return context


context_chain = RunnableParallel({
    'context': retriever | RunnableLambda(format_text),
    'question': RunnablePassthrough()
})

main_chain = context_chain | prompt | model | parser

with col1:
    if st.button("Send"):
        result = main_chain.invoke(question)
        # print(result)
        st.write(result)
