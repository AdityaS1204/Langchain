from pydantic import BaseModel,EmailStr,Field
from typing import Optional


class Student(BaseModel):
    name:str
    age:Optional[str] = int
    email:EmailStr
    cgpa:float = Field(gt=0,lt=10)
    
new_student = {'name':'aditya','age':'0','email':'aditya@mail.com','cgpa':7}

student = Student(**new_student)
json = student.model_dump_json()
dictionary = student.model_dump()
print(type(dictionary))
print(json)    