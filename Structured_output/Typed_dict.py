from typing import TypedDict

class person(TypedDict):
    
    name:str
    age:int
    student:bool

new_person: person = {'name':'aditya singh','age':20,'student':True}    

print(new_person)