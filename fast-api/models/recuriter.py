from pydantic import BaseModel
class Recuriter(BaseModel):
    username:str
    email:str
    password:str
