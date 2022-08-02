class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance):
      self.int_rate = int_rate
      self.balance=balance
      BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdraw(self, amount):
        if self.balance>=amount:
          self.balance-=amount
        else:
          self.balance-=5
          print("you broke!")
    def display_account_info(self):
        print("balance:" ,self.balance)
        print("interest:" ,self.int_rate * 100,"%")
        return self
    def yield_interest(self):
        if self.balance<=0:
          print("Try again next time")
        else:
          self.balance+=self.balance*self.int_rate
          self.display_account_info()
        return self
  @classmethod
  def print_all_instances(cls):

acc1 = BankAccount(.02,100).deposit(300).withdraw(200).display_account_info()
acc2 = BankAccount()
acc3=BankAccount()