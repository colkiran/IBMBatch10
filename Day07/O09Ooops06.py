
class Player:
    team = "India"
    def __init__(self, name, age):
        self.name  = name
        self.age = age
        print(f"Player Ctor......")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}\nTeam is {Player.team}")

    @classmethod
    def createPlayer(cls, fn, ln, age):
        print("factory.....")
        return cls(f"{fn} {ln}", age)              # this will call the constructor


ply1 = Player("Sachin", 35)
ply1.get_details()

print("-" * 60)
# wanted to accept name in the form of first name and last name
ply2 = Player.createPlayer("Rohit", "Sharma", 38)
ply2.get_details()







