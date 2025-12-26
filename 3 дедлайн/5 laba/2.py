class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Недостаточно средств")
    
    def get_balance(self):
        return self.balance

account = BankAccount("Likov", 100)
account.deposit(50)
account.withdraw(200)
account.withdraw(30)
print(account.get_balance())