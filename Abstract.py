# from abc import ABC, abstractmethod

# class bankAccount(ABC):

#     def withdraw(self,amount):
#         pass

#     def deposit(self,amount):
#         pass

# class SavingAccount(bankAccount):
#     def __init__(self,balance):
#         self.balance = balance
#     def withdraw(self, amount):
#         if amount<= self.balance:
#             self.balance -= amount
#             print("Withdrawn:",{amount})

#         else:
#             print("Insufficeint balance")
#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposited:",{amount})

# account =  SavingAccount(5000)
# account.deposit(100)
# account.withdraw(300000)
# print("Currebt balance:", account.balance)


class India():
    def capital(self):
        print("New delhi is the capital city")

    

    def language(self):
        print("Hindi is the main language")

    def type(self):
        print("India is the developing country.")    


class USA():
    def capital(self):
        print("Washington DC is the capital city")

    

    def language(self):
        print("English is the main language")

    def type(self):
        print("USA is the developed country.")

obj_Ind = India()
obj_usa =  USA()

for country in(obj_Ind,obj_usa):
    country.capital()
    country.language()
    country.type()
