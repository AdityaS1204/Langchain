from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

class review(TypedDict):
    
    summary:str
    sentiment:str
    
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-001')

structured_model = model.with_structured_output(review)

result = structured_model.invoke(""" The hardware is great, but the software feels bloated. There are many pre-installed apps that i can't remove. Also the UI looks outdated.Hoping a software update to fix this.""") 

print(result)