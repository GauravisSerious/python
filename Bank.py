#an simple bank project to understand OOps concept and Class inheritance!





class Account:
    def __init__(self,name,balance,min_balance):
        self.name=name
        self.balance=balance
        self.min_balance=min_balance
    
    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        if self.balance - amount >= self.min_balance:
            self.balance-=amount
        else:
            print("Not enough credits aavailable")
    
    def statement(self):
        print("Account balance:{}".format(self.balance))

class current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance,min_balance = -1000)
    def __str__(self):
        return "{}'s current account: Balance ${}".format(self.name,self.balance)


class savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance,min_balance=0)
        

#USAGE 
# x = savings("Gaurav",10000)
# x.deposit(3000)
# x.statement()
# x.withdraw(14000)
# # x.statement()
