from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system','you are helpfull {domain} expert'),
    ('human','Explain in simple words, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'LBW'})

print(prompt)