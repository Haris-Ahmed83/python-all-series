class car:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
    
    def drive(self):
        print(self.brand, "is driving at", self.speed, "km/h")

s1 = car("BMW",180)
s1.drive()

