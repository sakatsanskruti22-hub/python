class account:
    def __init__(self,balance):
        self.balance=balance

    def get_balance(self):
        return self.balance    
    
    def set_balance(self,amount):
        self.balance=amount
        print("Balance updated Successfully")

    def  __private_method(self):
        return "hello i'm private method"
    def access_private_method(self):
        return self .__private_method()
    
    def __withdraw(self,amount):
        if amount > self.__balance:
            print("debited:",amount,"remaining is",self.__balance)"
            else:
            print("insufficient balance:")

    def __deposite(self,amount):
        self.balance+=amount
        print("deposited successfully")

obj=account(500)
print(obj.get_balance())
obj.set_balance(500)
print(obj.get_balance())
print(obj.access_private_method())
obj._account__withdraw(500)
print(obj.get_balance())
obj._account__deposite(3000)
print(obj.get_balance())           

