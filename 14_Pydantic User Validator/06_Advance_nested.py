from pydantic import BaseModel
from typing import Optional,list,Union

class Address(BaseModel):
    street:str
    city:str
    postal_code:str

class Company(BaseModel):
    name : str
    address:Optional[Address]= None

class Employee(BaseModel):
    name:str
    address:Optional[Company]=None

class TextContent(BaseModel):
    type:str
    url:str
    alt_text:str

class ImageContent(BaseModel):
    type:str ="Image"
    url :str
    alt_text : str

class Articale(BaseModel):
    title :str
    sections:list[Union[TextContent,ImageContent]]

class Country(BaseModel):
    name : str
    code : str

class State (BaseModel):
    name :str
    counrty:Country

class City(BaseModel):
    name:str
    state:State

class Address(BaseModel):
    name :str
    city:City
    postal_code:str

class Organization(BaseModel):
    name: str
    head_quarter:Address
    brancher:list[Address]=[]
    







