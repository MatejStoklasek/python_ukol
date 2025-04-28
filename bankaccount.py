class BankAccount:
    def __init__(self, account_holder, initial_balance=0,):
        self.account_holder = account_holder
        self.__balance = initial_balance  # private attribute

    def deposit(self, amount):
        if amount < 0:
            print(f"({self.account_holder})Deposit amount must be positive")
            return

        self.__balance += amount
        print(f"({self.account_holder})Deposit accepted, New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount < 0 :
            print(f"({self.account_holder})Withdraw amount must be positive")
            return

        if amount > self.__balance :
            print(f"({self.account_holder})Insufficient balance")
            return

        self.__balance -= amount
        print(f"({self.account_holder})Withdraw accepted, New balance: {self.__balance}")

    def transfer(self,other_account, amount):
        if amount < 0:
            print("Transfer amount must be positive")
            return
        other_account.withdraw(amount)
        self.__balance += amount
        print(f"Transfer accepted, New balance: {self.__balance}")
        print(f"({other_account.account_holder})Transfer accepted, New balance: {self.__balance})")


#
#
#
#
ba = BankAccount("Jan" ,100)
ba2 = BankAccount("Zuzana", 600)

ba.deposit(100)
ba.transfer(ba2, 200)

ba.deposit(100)
#ba2.deposit(200)


