
class Player:

    team = "India"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")


ply1 = Player("Virat", 36)
ply1.get_details()

print("-" * 60)
ply2 = Player("Rohit", 38)
ply2.get_details()

print("-" * 60)
print(f"Player :{Player.team}")
print(f"ply1   :{ply1.team}")
print(f"ply2   :{ply2.team}")

print("-" * 60)
Player.team = "MI"
print(f"Player :{Player.team}")
print(f"ply1   :{ply1.team}")
print(f"ply2   :{ply2.team}")

print("-" * 60)
ply1.team = 'RCB'
print(f"ply1 :{ply1.team}")
print(f"Player :{Player.team}")
print(f"ply2   :{ply2.team}")

print("-" * 60)
print(f"ply1 :{ply1.__dict__}")

