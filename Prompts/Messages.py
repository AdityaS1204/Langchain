from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

messages = [
    SystemMessage(content='you are an ai assistant'),
    HumanMessage(content="tell me about langGraph")
]

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-001')

result = model.invoke(messages)
print(result.content)
messages.append(AIMessage(content=result.content))
print()
print(messages)
