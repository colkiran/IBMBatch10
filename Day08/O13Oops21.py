# duck types

from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def doJob(self):
        pass

class Manager(Employee):
    def doJob(self):
        print("Managers job.....")


class Developer(Employee):

    def doJob(self):
        print("Developers job.....")


def BankJob(emps):       # polymorphism
    print("Bank job started.......")
    for emp in emps:
        emp.doJob()
    print("Bank job completed........")
    print("-" * 60)

mike = Manager()
david = Developer()

BankJob([mike, david])

