print("---Wellcome---")
user = "Admin"
password ="1234"
attemps = 0
max_limits = 3
while attemps < max_limits:
    username = input("Enter the Username:")
    password = input("Enter your password:")

    if username ==user and password ==  password:
        print("login Sucessfully")
        break
    else:
        print("invilid user name or password")
        if attemps == max_limits:
            print("Try again later")
