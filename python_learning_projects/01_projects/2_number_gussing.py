import random
secret_number = random.randint(1,100)
attemps = 0
while True:
    guess = int(input("Enter your guess: "))
    attemps +=1
    if guess == secret_number:
        print("👏 you won ✔ ")
        print("attemps",attemps)
        break
    elif guess < secret_number:
        print("😒Too low")
    elif guess > secret_number:
        print("🤷‍♂️ Too High")
    else:
        print("invlid number")
