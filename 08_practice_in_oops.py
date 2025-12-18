# Requirements:
# Class: Student
# Attributes: name, roll_no, marks
# Method: display_info()
# Practice Goal:
# Create 2–3 student objects and display their data.

# class Student:
#     def __init__(self,name,roll_no,marks):
#         self.name = name
#         self.roll_no = roll_no
#         self.marks = marks
#     def namespace(self):
#         print("my name is ",self.name)
#         print("my roll num is ",self.roll_no)
#         print("my marks is ",self.marks)

# p1 = Student("maryum",24651,890)
# print("my naem is", {p1.name}," and my roll num is", {p1.roll_no} ,"and my marks is ",{p1.marks})
# p1.namespace()

class Student:
    def __init__(self, name, rollnum, marks):
        self.name = name
        self.rollnum = rollnum
        self.marks = marks

    def calculate_percentage(self):
        return (self.marks / 1000) * 100

    def check_result(self):
        percentage = self.calculate_percentage()
        if percentage >= 40:
            return "PASS"
        else:
            return "FAIL"

    def get_grade(self):
        percentage = self.calculate_percentage()
        if 80 <= percentage <= 100:
            return "A+"
        elif 60 <= percentage < 80:
            return "B+"
        elif 40 <= percentage < 60:
            return "C"
        else:
            return "F"

    def display_info(self):
        print("Name:", self.name)
        print("Roll No:", self.rollnum)
        print("Marks:", self.marks)
        print("Percentage:", self.calculate_percentage(), "%")
        print("Grade:", self.get_grade())
        print("Result:", self.check_result())
        print("-" * 30)

p1 = Student("Maryum", 990, 980)
p2 = Student("Ali", 691, 690)
p3 = Student("Daniyal", 4212, 240)
p4 = Student("Ayza", 729, 190)

p1.display_info()
p2.display_info()
p3.display_info()
p4.display_info()

