# from typing import Union
#
# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# from fastapi import FastAPI
# from pydantic import BaseModel
#
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#
#
# app = FastAPI()
#
#
# @app.post("/items/")
# async def create_item(item: Item):
#     return item

# from typing import Annotated
#
# from fastapi import FastAPI, Form
#
# app = FastAPI()
#
#
# @app.post("/login/")
# async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
#     return {"username": username}
# from fastapi import FastAPI, HTTPException
#
# app = FastAPI()
#
# items = {"foo": "The Foo Wrestlers"}
#
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in items:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return {"item": items[item_id]}

# from fastapi import FastAPI,Depends,HTTPException,status
# from fastapi.security import HTTPBasic,HTTPBasicCredentials
#
# app=FastAPI()
#
# security=HTTPBasic()
#
# def authenticate(credentials:HTTPBasicCredentials=Depends(security)):
#                  correct_username="username"
#                  correct_password="password"
#                  if credentials.username!=correct_username or credentials.password!=correct_password:
#                     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="incorrect username or password",headers={"www-Authenticate":"Basic"},)
#                  return True
# @app.get("/login")
# def login(credentials:HTTPBasicCredentials=Depends(security)):
#    if authenticate(credentials):
#       return {"message":"Login Suceesful"}

# from fastapi import FastAPI, HTTPException
#
# app = FastAPI()
#
# users_db = {
#     "username1": "password1",
#     "username2": "password2"
# }
#
# @app.post("/login")
# def login(username: str, password: str):
#     if username in users_db and users_db[username] == password:
#         return {"message": "login successful"}
#     else:
#         raise HTTPException(status_code=401, detail="incorrect username or password")

# from fastapi import  FastAPI
# from pydantic import BaseModel
# app=FastAPI()
# class CompanyAccount(BaseModel):
#     company_name:str
#     company_website:str
#     phone_number:str=None
# @app.post("/create_company_account")
# def create_company_account(company_data:CompanyAccount):
#     return company_data



