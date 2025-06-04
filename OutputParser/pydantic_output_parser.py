from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-001')

class person(BaseModel):
    name:str = Field(description='name of the person')
    age: int = Field(gt=18,description='age of the person')
    city: str = Field(description='city of the person')
    
parser = PydanticOutputParser(pydantic_object=person)

template = PromptTemplate(
    template='generate name age and city of a {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)    

prompt = template.invoke({'place':'indian'})

result = model.invoke(prompt)
final_result = parser.parse(result.content) # type: ignore
print(final_result)
print(type(final_result))