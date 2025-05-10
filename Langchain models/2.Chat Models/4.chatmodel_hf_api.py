from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get Hugging Face API key from environment variables
api_key = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

# Ensure API key is not None
if api_key is None:
    raise ValueError("Hugging Face API key not found. Set HUGGINGFACEHUB_API_TOKEN in .env file.")



llm = HuggingFaceEndpoint(
    repo_id='microsoft/phi-2',
      huggingfacehub_api_token=api_key,
  task='text-generation'  
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("what is the capital of india")

print(result.content)



# import requests

# url = "https://api-inference.huggingface.co/models/microsoft/phi-2"
# headers = {"Authorization": "Bearer "}
# data = {"inputs": "What is the capital of India?"}

# response = requests.post(url, headers=headers, json=data)
# print(response.json())