from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str

class ProductCreate(BaseModel):

    title: str
    description: str
    price: float
    stock: int

class ProductUpdate(BaseModel):

    title: str
    description: str
    price: float
    stock: int

class UserUpdate(BaseModel):

    name: str
    email: str