print("---Temperature Converter---")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter 1 or 2: ")

# Step 2: Input temperature
temp = float(input("Enter the temperature: "))

# Step 3: Convert based on choice
if choice == "1":
    converted = (temp * 9/5) + 32
    print(f"{temp}°C = {converted:.2f}°F")
elif choice == "2":
    converted = (temp - 32) * 5/9
    print(f"{temp}°F = {converted:.2f}°C")
else:
    print("Invalid choice! Please enter 1 or 2.")
