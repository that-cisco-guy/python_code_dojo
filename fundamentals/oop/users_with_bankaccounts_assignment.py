class BankAccount:
    def __init__(self, int_rate = 0.01, checking_balance = 0, saving_balance = 0):
        self.int_rate = int_rate
        self.checking_balance = checking_balance
        self.saving_balance = saving_balance
    def check_deposit(self, amount):
        self.checking_balance += amount
        return self
    def check_withdrawl(self, amount):
        if self.checking_balance - amount > 0:
            self.checking_balance -= amount
        else:
            print('Insufficient Funds!')
        return self
    def save_deposit(self, amount):
        self.saving_balance += amount
        return self
    def save_withdrawl(self, amount):
        if self.saving_balance - amount > 0:
            self.saving_balance -= amount
        else:
            print('Insufficient Funds!')
        return self
    def display_account_info(self):
        print(f'Checking Balance:{self.checking_balance} Saving Balance:{self.saving_balance}, Interest Rate:{self.int_rate}')
        return self
    def yield_interest(self):
        if self.saving_balance > 0:
            self.saving_balance =  (self.saving_balance * self.int_rate) + self.saving_balance
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, checking_balance = 0, saving_balance = 0)
    def make_checkDeposit(self, amount):
        self.account.check_deposit(amount)
    def make_checkWithdrawl(self,amount):
        self.account.check_withdrawl(amount)
    def make_saveDeposit(self, amount):
        self.account.save_deposit(amount)
    def make_saveWithdrawl(self,amount):
        self.account.save_withdrawl(amount)
    def display_user_balance(self):
        print(self.name) , self.account.display_account_info()
    def transfer_checkMoney(self,amount,other_user):
        other_user = other_user
        if self.account.checking_balance > 0:
            self.account.checking_balance -= amount
            other_user.account.checking_balance += amount
            print(f'Transferred {amount} to {other_user.name} Checking')
    def transfer_saveMoney(self,amount,other_user):
        other_user = other_user
        if self.account.saving_balance > 0:
            self.account.saving_balance -= amount
            other_user.account.saving_balance += amount
            print(f'Transferred {amount} to {other_user.name} Saving')


jerry = User('Jerry', 'jerry@jerryemail.com')
jerry.make_checkDeposit(100)
jerry.make_checkWithdrawl(25)
jerry.make_saveDeposit(500)
jerry.make_saveWithdrawl(50)
jerry.display_user_balance()
niko = User('niko', 'niko@nikoemail.com')
niko.make_checkDeposit(100)
niko.make_checkWithdrawl(25)
niko.make_saveDeposit(500)
niko.make_saveWithdrawl(50)
niko.display_user_balance()
jerry.transfer_checkMoney(25,niko)
jerry.transfer_saveMoney(25,niko)
jerry.display_user_balance()
niko.display_user_balance()
