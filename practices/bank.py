class bank:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.acc_no = int(input("Enter your account number: "))
        self.balance = float(input("Enter your balance: "))

    def deposit(self, balance , amount):
        self.balance = self.balance + amount
        a= "The balance amount is : "+ str(self.balance)
        print(a)


    def withdraw(self, balance  , amount ):
        if amount > self.balance:
            print("You don't have enough money")
        else:
            self.balance = self.balance - amount
            a = "The balance amount is : " + str(self.balance)
            print(a)



obj = bank()
obj.deposit(obj.balance, 1000)
obj.withdraw(obj.balance, 1000)


