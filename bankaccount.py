class BankAccount:
    def __init__(self, account_holder, initial_balance=0, ):
        self.account_holder = account_holder
        self.__balance = initial_balance  # private attribute

    def deposit(self, amount):
        if amount < 0:
            print(f"({self.account_holder})Deposit amount must be positive")
            return

        self.__balance += amount
        print(f"({self.account_holder})Deposit accepted, New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount < 0:
            print(f"({self.account_holder})Withdraw amount must be positive")
            return

        if amount > self.__balance:
            print(f"({self.account_holder})Insufficient balance")
            return

        self.__balance -= amount
        print(f"({self.account_holder})Withdraw accepted, New balance: {self.__balance}")

    def transfer(self, other_account, amount):
        if amount < 0:
            print("Transfer amount must be positive")
            return
        other_account.withdraw(amount)
        self.__balance += amount
        print(f"Transfer accepted, New balance: {self.__balance}")
        print(f"({other_account.account_holder})Transfer accepted, New balance: {self.__balance}")


#
#
#
#
#
#
bank_accounts = [BankAccount(account_holder="<Jon>", initial_balance=1000), ]


def menu():
    print("Vítejte v Bance!")
    print("1 - seznam účtů ")
    print("2 - přidat účet")
    print("3 - převod financí")
    print("4 - výběr financí")
    print("5 - vklad financí")

    choice =int(input("Zvolte akci:"))
    if choice == 1:
        # TODO: seznam
        print_accounts()
    elif choice == 2:
        # TODO: přidat účet
        add_account()
        print("")
    elif choice == 3:
        # TODO: převod
        transfer()
        print("")
    elif choice == 4:
        # TODO: výběr
        transfer()
        print("")
    elif choice == 5:
        # TODO: vklad
        transfer()
        print("")
    else:
        print("Chybná akce, vyber znovu")

    menu()

def print_accounts():
    i = 0
    for bank_account in bank_accounts:
        print(f"{i}. {bank_accounts.account_holder}")
        i += 1

def add_account():
    name = input("Název účtu: ")
    bank_accounts.append(BankAccount(account_holder=name, initial_balance=1000))

def transfer():
    print("Dostupných účtů")
    print_accounts()

    index_from = input("Účet ze kterého:")
    index_to = int("Účet do kterého")
    amount = input("Částka:")

    bank_accounts[int(index_to)].transfer(bank_accounts[int(index_from)], int(amount))


menu()

