from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional

class Patient(BaseModel):
    p_id: Annotated[int, Field(..., description="ID of the patient")]
    name: Annotated[str, Field(..., description="Name of the patient")]
    city: Annotated[str, Field(..., description="City where the patient is living")]
    age: Annotated[int, Field(..., gt=0 , lt=120, description="Age of the patient")]
    gender: Annotated[Literal['male','female', 'others'], Field(..., description="Gender of the patient")]
    height: Annotated[float, Field(..., gt=0, description="Height of the patient in meters")]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the patient in kgs")]


    @computed_field
    @property
    def verdict(self) ->str:
        bmi = round(self.weight/(self.height**2),2)
        if bmi < 18.5:
            return "underweight"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Normal"
        else:
            return "obese"

class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None)]
    gender: Annotated[Optional[Literal['male','female', 'others']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None)]
    weight: Annotated[Optional[float], Field(default=None)]

class DoctorRegister(BaseModel):
    username:str = Field(..., min_length=3)
    password:str = Field(..., min_length=8)

class DoctorLogin(BaseModel):
    username:str = Field(..., min_length=3)
    password:str = Field(..., min_length=8)


