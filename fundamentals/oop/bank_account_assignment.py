class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdrawl(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
        else:
            print('Insufficient Funds!')
        return self
    def display_account_info(self):
        print(self.balance)
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance =  (self.balance * self.int_rate) + self.balance
        return self
    def display_all_info(self):
        print(self.int_rate, self.balance)
        return self
jerry = BankAccount()
niko = BankAccount()
jerry.deposit(100).deposit(100).deposit(100).withdrawl(100).yield_interest().display_account_info()
niko.deposit(200).deposit(200).withdrawl(25).withdrawl(25).withdrawl(25).withdrawl(25).yield_interest().display_account_info()
jerry.display_all_info()
niko.display_all_info()
