from pydantic import BaseModel
class Product(BaseModel):
    id : int
    Name :str
    price : float
    in_stock : bool = True

product_1 = Product(id= 101,Name = "Laptop",price = 20.00,in_stock=True)
product_2 = Product(id= 102,Name = "Mouse",price = 15.50,in_stock=True)
product_3 = Product(id= 103,Name = "Keyboard",price = 8.90,in_stock=True)
product_4 = Product(id= 104,Name = "Speakers",price = 10.00,in_stock=False)
product_5 = Product(id= 105,Name = "Headphones",price = 6.30,in_stock=False)
print(product_1)
print(product_2)
print(product_3)
print(product_4)
print(product_5)