from pydantic import BaseModel

class Persons(BaseModel):
    rollnumber: int
    fullname: str
    age: int
    profession: str


class ReadPersons(BaseModel):
    rollnumber: int
    fullname: str
    age: int
    profession: str
    class Config:
        from_attributes = True


