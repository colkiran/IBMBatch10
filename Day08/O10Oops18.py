
class Animal:

    def __init__(self):
        print("Animal Ctor.....")
        self.a = 10

    def eat(self):
        print("Animals eat.....")

    def fun(self):
        print("Animal class fun method")


class Person:

    def __init__(self):
        print("Person Ctor.....")
        self.p = 20

    def walk(self):
        print("Person walks........")

    def fun(self):
        print("Person class fun method.....")

class Girl(Animal, Person):

    def __init__(self):
        super().__init__()
        Person.__init__(self)
        print("Girl Ctor......")
        self.g = 30

    def talk(self):
        print("Girl talks.....")

tina = Girl()
tina.eat()
tina.walk()
tina.talk()
print("-" * 60)

tina.fun()

print("-" * 60)
print(tina.__dict__)
