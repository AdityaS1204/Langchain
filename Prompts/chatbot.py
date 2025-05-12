from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-001')

while True:
    user_input = input("you: ")
    if user_input == 'exit':
        break
    else:
        result = model.invoke(user_input)
        print("AI: ",result.content)