#带利息的账户
class Account:
    def __init__(self,balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def deposit(self,amount):
        if amount<=0:
            print("存款额必须大于0")
        else:
            self.__balance += amount
class SavingsAccount(Account):
    def add_interest(self,rate):
        self.deposit(self.get_balance()*rate)


account = SavingsAccount(100)
print(f"{account.get_balance():.2f}")
account.deposit(50)
print(f"{account.get_balance():.2f}")
account.add_interest(0.1)
print(f"{account.get_balance():.2f}")
account.deposit(-20)
print(f"{account.get_balance():.2f}")