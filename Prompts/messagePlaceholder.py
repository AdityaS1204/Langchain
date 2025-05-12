from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

chat_history = []
query = 'what is the delivery status of my order'
chat_template = ChatPromptTemplate([
    ('system','you are an helpfull customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())
print(chat_history)


 

prompt = chat_template.invoke({'chat_history':chat_history,'query':query})
print(prompt)