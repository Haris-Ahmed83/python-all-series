import random
import string

letter = string.ascii_letters
number = string.digits
punc = string.punctuation

length = int(input("Enter a length of password"))
password = ""
character = letter+number+punc

for i in range(length):
    password += random.choice(character)
print("Generated password",password)
