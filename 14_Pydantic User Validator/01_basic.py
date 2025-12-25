from pydantic import BaseModel
class User(BaseModel):
    name : str
    age : int
user = User(name ="hxrry",age = "21")
print(user)


