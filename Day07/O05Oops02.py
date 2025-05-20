
class Player:

    def __init__(self):         # constructor
        print("Player Initialized........")

    def get_runs(self):
        print("runs scored.....")

    def __del__(self):              # destructor
        print("object destroyed.......")

sachin = Player()
sourav = Player()
sachin.__init__()

print("-" * 60)
sachin.get_runs()
sourav.get_runs()

print("-" * 60)
del sachin

print("-" * 60)
