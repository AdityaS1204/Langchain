import streamlit as st
from ui import show_ui
from qa_chain import build_qa_chain
from youtube_utils import extract_yt_video_id,transcript_chunks
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title='Youtube Chatbot',layout='centered')
st.header('Chat with Youtube videos')

yt_video,language,question = show_ui()

if st.button('send'):
    if not yt_video or not question:
        st.warning("please enter both a video url and your question")
    else:
        with st.spinner("Processing..."):
            try:
                video_id = extract_yt_video_id(yt_video)
                chunks = transcript_chunks(video_id,language)
                qa_chain = build_qa_chain(chunks)
                result = qa_chain.invoke(question)
                st.success("Response:")
                st.write(result)
            except Exception as e:
                st.error(f"Error:{str(e)}")        