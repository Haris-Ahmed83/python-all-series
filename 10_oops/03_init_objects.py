class Student:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    def show(self):
        print("name",self.name)
        print("age",self.age)

s1 = Student("Hxrry",20)
s1.show()