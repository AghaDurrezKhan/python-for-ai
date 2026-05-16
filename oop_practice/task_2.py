import pandas as pd
from datetime import datetime

class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        self.transactions = []

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Error: Balance cannot be negative")

    @classmethod
    def from_dict(cls, data):
        account = cls(data["owner"])
        account.balance = data["balance"]
        return account

    @staticmethod
    def validate_deposit(deposit):
        if isinstance(deposit, (int, float)):
            if deposit > 0:
                return True
            else:
                return False
        else:
            return False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"{datetime.now()} - Deposited ${amount}")
        else:
            print("Error: Amount Cannot be Negative")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"{datetime.now()} - Withdrew ${amount}")
        else:
            print("Error: Insufficent Balance")

    def get_transactions(self):
        return self.transactions
    
    def __str__(self):
        return f"Owner: {self.owner} | Balance: ${self.balance:,.2f}"
    

class SavingsAccount(BankAccount):
    def __init__(self, owner):
        super().__init__(owner)
        self.interest_rate = 0.05

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transactions.append(f"{datetime.now()} - Interest of ${interest} applied")

    def __str__(self):
        return f"{super().__str__()} | Rate: {self.interest_rate*100}%"
    
bank_account = BankAccount("George")
savings_account = SavingsAccount("Robert")

bank_account.deposit(5700)
bank_account.withdraw(200)

savings_account.deposit(7000)
savings_account.withdraw(500)

bank_account.withdraw(10000)
bank_account.deposit(-1000)

savings_account.apply_interest()

print(bank_account.get_transactions())
print(savings_account.get_transactions())

data = {
    "owner": savings_account.owner,
    "balance": savings_account.balance,
    "transactions": savings_account.get_transactions(),
    "rate": savings_account.interest_rate*100
}

data2 = {
    "owner": bank_account.owner,
    "balance": bank_account.balance,
    "transactions": bank_account.get_transactions(),
}
df = pd.DataFrame([data, data2])

bank_account.validate_deposit("uishc")