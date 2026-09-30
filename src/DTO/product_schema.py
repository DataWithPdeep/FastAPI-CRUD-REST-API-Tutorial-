from pydantic import BaseModel, EmailStr

class CreateProduct(BaseModel):
    name:str
    price:int = 0
    category:str
    stock:int=0

class UpdateProduct(BaseModel):
    name:str = None
    price:int = None
    category:str = None
    stock:int = None

class OrderSchema(BaseModel):
    count:int = None
    product_id:int = None
    email:EmailStr=None
