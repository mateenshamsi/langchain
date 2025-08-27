from pydantic import BaseModel,EmailStr,Field
from typing import Optional 
# Define a Student model
class Student(BaseModel):
    name: str="nitish"
    age:Optional[int]=None
    email:EmailStr
    cgpa:float=Field(gt=0,lt=10,default=5,description="A decimal value represnting the cgpa of student")
# Create a dictionary
new_student = {'name': 'nitish','email':"abc@gmail.com"}  

# Unpack the dictionary into the model
student = Student(**new_student)
student_dict = dict(student)

print(student_dict['age'])
