#!/usr/bin/python3
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}, New balance is ${self.balance}"
        return "invalid deposit amount."
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}, New balance is ${self.balance}."
        return "Invalid withdrawal amount or insufficient funds"
    
    def get_balance(self):
        return f"The current balance is ${self.balance}."
    
my_account = BankAccount(account_number="123456789", account_holder="Jace Jeje", balance=1000)
my_account2 = BankAccount(account_number="987654321", account_holder='Jireh Jeje')
print(my_account.deposit(500))

print(my_account.withdraw(200))

print(my_account.get_balance)

print(my_account2.get_balance)

print(my_account2.deposit(5000))
