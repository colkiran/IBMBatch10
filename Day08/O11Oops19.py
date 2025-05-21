"""
abc - module
ABC - class
abstractmethod - method
"""
from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self):
        print("Follow RBI rules.....")
    @abstractmethod
    def getBalance(self):
        pass

    def deposit(self):
        pass

class SavingsAccount(Account):

    def deposit(self):
        print("Amount credited successfully....")

    def getBalance(self):
        print("The balance is ######.##")

sav = SavingsAccount()
sav.getBalance()
sav.deposit()
