class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Current Balance:", self.balance)

# Create account
acc = BankAccount(101, "Aditya", 1000)

# Deposit money
acc.deposit(500)

# Withdraw money
acc.withdraw(300)

# Check balance
acc.check_balance()
