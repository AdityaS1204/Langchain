from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()

model = ChatAnthropic(model='3.5-sonnet-20241012')

result = model.invoke("what is the capital of india ?")

print(result.content)