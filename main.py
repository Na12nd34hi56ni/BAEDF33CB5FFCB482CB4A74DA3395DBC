class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

# Creating an instance of BankAccount with an initial balance of $1000
account = BankAccount(1000)

# Depositing $500 into the account
if account.deposit(500):
    print("Deposited $500. New balance:", account.balance)
else:
    print("Invalid deposit amount")

# Withdrawing $200 from the account
if account.withdraw(200):
    print("Withdrew $200. New balance:", account.balance)
else:
    print("Invalid withdrawal amount")

# Attempting to withdraw $10000 (more than the balance)
if account.withdraw(10000):
    print("Withdrew $10000. New balance:", account.balance)
else:
    print("Invalid withdrawal amount")
