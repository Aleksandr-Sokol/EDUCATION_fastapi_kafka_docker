from pydantic import BaseModel

class Message(BaseModel):
    message : str


class User(BaseModel):
    name: str
    family: str
    age: int
