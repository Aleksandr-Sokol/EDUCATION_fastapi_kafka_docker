from pydantic import BaseModel

class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    name: str
    family: str
    age: int

    class Config:
        orm_mode = True


class DataSchema(UserSchema):
    id: int
