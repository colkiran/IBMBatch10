
"""
Recap
-----
1. class
2. object
3. isinstance
4. __init__
5. self
6. class attributes / class variables
7. @classmethod
8. cls
9. __str__
10. __eq__, __gt__, __ge__ (@total_ordering)
11. __add__, __sub__, __mul__, __truediv__
12. __iter__, append, __setitem__,___getitem__, __len__
13. private variable __var
14. __dict__
15. property(), @property, setter, deleter
"""

# inheritance

class Animal:

    def __init__(self):
        print("Animal Ctor.....")
        self.age = 1

    def eat(self):
        print("Animals eat......")

# inheritance

class Bird(Animal):

    def fly(self):
        print("Birds fly......")

class Fish(Animal):

    def swim(self):
        print("Fishes swim......")

print('-' * 60)
cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()

print('-' * 60)
dolphin = Fish()
dolphin.eat()
dolphin.swim()

print('-' * 60)
print(cuckoo.__dict__)
print(dolphin.__dict__)

print('-' * 60)
print(f"isinstance(cuckoo, Bird) :{isinstance(cuckoo, Bird)}")
print(f"isinstance(cuckoo, Animal) :{isinstance(cuckoo, Animal)}")
print(f"isinstance(cuckoo, object) :{isinstance(cuckoo, object)}")
print(f"isinstance(cuckoo, Fish) :{isinstance(cuckoo, Fish)}")

print('-' * 60)
print(f"isinstance(dolphin, Fish) :{isinstance(dolphin, Fish)}")
print(f"isinstance(dolphin, Animal) :{isinstance(dolphin, Animal)}")
print(f"isinstance(dolphin, object) :{isinstance(dolphin, object)}")
print(f"isinstance(dolphin, Bird) :{isinstance(dolphin, Bird)}")

print('-' * 60)
print(f"issubclass(Bird, Animal) :{issubclass(Bird, Animal)}")
print(f"issubclass(Bird, object) :{issubclass(Bird, object)}")
print(f"issubclass(Bird, Fish) :{issubclass(Bird, Fish)}")
