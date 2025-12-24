obtain_marks = float(input("Enter your obtain marks:-"))
total_marks= float(input("Enter your total marks:-"))
#persentage
persentage = obtain_marks/total_marks*100
#grade
if persentage >= 90:
    Grade ="A🍉"
elif persentage >=75:
    Grade ="B"
elif persentage >=50:
    Grade= "C" 
else:
    Grade = "fail"
print(f"percentage:-{persentage:.2f}%")
print(f"Grade:-{Grade:}")