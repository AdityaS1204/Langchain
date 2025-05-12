from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate,load_prompt
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-001')

st.header("Research Tool")
# user_input = st.text_input("Enter your prompt") static prompt

paper_input = st.selectbox('Select Research paper name',["Attnetion is all you need","BERT: Pre-training of bidirectional transformers","GPT-3: Language models are few-shot learners","Diffusion models beat GANs on Image synthesis"])

style_input = st.selectbox("Select explaination style",["Beginner-frinedly","code-oriented","Technical","Mathematical"])

length_input = st.selectbox("Select length",["Short(1-2 paragraph)","medium(3-5 paragraph)","Long (Detail Explaination)"])


template = load_prompt('Prompt_Template.json')


prompt = template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
})

if st.button("summarize"):
    result = model.invoke(prompt)
    st.write(result.content)

