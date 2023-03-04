import random
import datetime

# Define classes
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.account_number = random.randint(100000, 999999)
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append((datetime.datetime.now(), amount, "Deposit"))

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append((datetime.datetime.now(), amount, "Withdrawal"))
            print("Withdraw successful")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

    def get_transactions(self):
        return self.transactions

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def remove_account(self, account):
        self.accounts.remove(account)

    def get_total_balance(self):
        total_balance = 0
        for account in self.accounts:
            total_balance += account.get_balance()
        return total_balance

# Define functions
def display_menu():
    print("Welcome to the bank management system")
    print("1. Add account")
    print("2. Remove account")
    print("3. Deposit money")
    print("4. Withdraw money")
    print("5. Check balance")
    print("6. View transactions")
    print("7. Quit")

def create_account():
    name = input("Enter name: ")
    balance = float(input("Enter initial balance: "))
    account = Account(name, balance)
    bank.add_account(account)
    print(f"Account created with account number {account.get_account_number()}")

def remove_account():
    account_number = int(input("Enter account number: "))
    for account in bank.accounts:
        if account.get_account_number() == account_number:
            bank.remove_account(account)
            print("Account removed")
            return
    print("Account not found")

def deposit():
    account_number = int(input("Enter account number: "))
    for account in bank.accounts:
        if account.get_account_number() == account_number:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
            print("Deposit successful")
            return
    print("Account not found")

def withdraw():
    account_number = int(input("Enter account number: "))
    for account in bank.accounts:
        if account.get_account_number() == account_number:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
            return
    print("Account not found")

def check_balance():
    account_number = int(input("Enter account number: "))
    for account in bank.accounts:
        if account.get_account_number() == account_number:
            balance = account.get_balance()
            print(f"Balance: {balance}")
            return
    print("Account not found")

def view_transactions():
    account_number = int(input("Enter account number: "))
    for account in bank.accounts:
        if account.get_account_number() == account_number:
            transactions = account.get_transactions()
            for transaction in transactions:
                print(transaction)
            return
    print("Account not found")

# Main program
bank = Bank("Green Bank")

while True:
    display_menu()
    choice = int(input("Enter choice: "))

    if choice == 1:
        create_account()
    elif choice == 2:
        remove_account()
    elif choice == 3:
        deposit()
    elif choice == 4:
        withdraw()
    elif choice == 5:
        check_balance()
    elif choice == 6:
        view_transactions()
    elif choice == 7:
        break
    else:
        print("Invalid Input")