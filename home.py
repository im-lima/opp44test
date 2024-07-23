class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance


class CheckingAccount(BankAccount):
    def __init__(self, account_number, owner, overdraft_limit, balance=0):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Overdraft limit exceeded")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, balance=0, interest_rate=0.02):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate
        print(f"Interest added. New balance: {self.balance}")


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def remove_account(self, account):
        self.accounts.remove(account)

    def list_accounts(self):
        for account in self.accounts:
            print(f"Account Number: {account.account_number}, Owner: {account.owner}, Balance: {account.balance}")

    def total_funds(self):
        total = sum(account.get_balance() for account in self.accounts)
        print(f"Total funds in the bank: {total}")
        return total


# Создаем счета
checking = CheckingAccount("CA54321", "Bob", 500, 200)
savings = SavingsAccount("SA12345", "Alice", 1000, 0.03)

# Создаем банк и добавляем счета
bank = Bank("MyBank")
bank.add_account(checking)
bank.add_account(savings)

# Действия с счетами
checking.withdraw(600)
checking.deposit(300)

savings.deposit(500)
savings.add_interest()
savings.withdraw(300)

# Выводим список счетов и общую сумму денег в банке
bank.list_accounts()
bank.total_funds()