first_number = int(input("Enter a first number:"))
second_number = int(input("Enter a second number:"))
operator = input("enter a operator:")
if operator == "+":
    result=(first_number +second_number)
    print(f"Answer of sum is :{result}")

elif operator == "-":
    result = (first_number - second_number)
    print(f"Answer of seb is: {result}")

elif operator =="/":
    result =(first_number / second_number)
    print(f"Answer of divide is :{result}")

elif operator =="*":
    result =(first_number / second_number)
    print(f"Answer of multiply is :{result}")

else:
    print("invlid operator")





