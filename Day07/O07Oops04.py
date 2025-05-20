
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

ply1 = Player("Sachin", 35)
ply1.get_details()

print("-" * 60)
ply2 = Player("Rahul", 32)
ply2.get_details()

"""
self - self will have the name of the object that called the method

ply1.get_detials() => self in get_details will have ply1 stored in it.

"""

print("-" * 60)
print(f"ply1 :{ply1.__dict__}")

print("-" * 60)
print(f"ply2 :{ply2.__dict__}")

print("-" * 60)
ply2.runs = 135
print(f"ply2 :{ply2.__dict__}")

print(f"ply1 :{ply1.__dict__}")
