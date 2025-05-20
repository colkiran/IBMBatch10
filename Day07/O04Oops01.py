
class Player:       # pascal casing

    def get_runs(self):
        print("Runs scored............")

sachin = Player()
sachin.get_runs()

print("-" * 60)
print(type(sachin))
print(sachin.__class__)

print("-" * 60)
print(__name__)         # current module name

print(f"isinstance(sachin, Player) :{isinstance(sachin , Player)}")
print(f"isinstance(sachin, object) :{isinstance(sachin , object)}")
print(f"isinstance(sachin, str)    :{isinstance(sachin , str)}")

