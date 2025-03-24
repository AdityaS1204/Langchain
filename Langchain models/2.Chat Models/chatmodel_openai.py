from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4')
# here the response is not just a string as it was while interacting with the llm.
#  here the respone is object with many values.

result = model.invoke("what is the capital of india ?")

print(result.content)
