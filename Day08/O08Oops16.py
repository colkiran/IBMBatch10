
class Animal:
    def __init__(self):
        print("Animal Ctor......")
        self.age = 1

    def eat(self):
        print("Animals eat.....")

class Bird(Animal):

    def __init__(self):      # overriding the parent class constructor
        super().__init__()
        print("Bird Ctor.....")
        self.weight = '3 kgs'

    def fly(self):
        print("Birds Fly.....")

cuckoo = Bird()
cuckoo.fly()
cuckoo.eat()

print(cuckoo.__dict__)
print(cuckoo.age)
print(cuckoo.weight)
