class bankaccount:
    def __init__(self,account_number,holder_name,balance=0):
        self.account_number =account_number
        self.holder_name =holder_name
        self.balance =balance
    def deposit(self,amount):
            self.balance+=amount
    def withdrawal(self,amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
         print("insufficient funds")
    def display_balance(self):
        print(f"account number:{self.account_number}")
        print(f"holders name:{self.holder_name}")
        print(f"balance:{self.balance}")

my_account =bankaccount("878372","alex",2332433)
my_account.display_balance()
my_account.deposit(5635234)
my_account.display_balance()
my_account.withdrawal(2424543)
my_account.display_balance()





