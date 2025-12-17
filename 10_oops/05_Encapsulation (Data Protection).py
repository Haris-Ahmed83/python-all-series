class bank:
    def __init__(self):
        self.__balance = 600

    def deposit(self,amount):
        self.__balance += amount

    def show_balance(self):
        print("Balance" ,self.__balance)

b  = bank()
b.deposit(500)
b.show_balance()



