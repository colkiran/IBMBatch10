
dct1 = dict()
print(f"dct1 :{dct1}")
print(type(dct1))

print("-" * 60)
dct2 = {'name': 'Sachin', 'age': 36, 'runs': 135, 'oppn': 'WI'}
print(f"dct2 :{dct2}")
print(type(dct2))

print("-" * 60)
dct3 = dict([('name', 'Rahul'), ('age', 32), ('runs', 85), ('oppn', 'AUS')])
print(f"dct3 :{dct3}")
print(type(dct3))

print("-" * 60)
dct4 = dict(name='Sourav', age=34, runs=105, oppn='Eng')
print(f"dct4 :{dct4}")
print(type(dct4))

print("-" * 60)
# CRUD

# create
player = {'name': 'Sachin', 'age': 34, 'runs': 125, 'oppn': 'WI'}
print(f"player :{player}")

print("-" * 60)
# Read
print(f"Name :{player['name']}")
print(f"Age  :{player['age']}")
print(f"Runs :{player['runs']}")

print("-" * 60)
for x in player:
    print(x, "=>", player[x])

print("-" * 60)
# Update = modify, add new key and value
player['runs'] = 99
player['oppn'] = 'Aus'
player['venue'] = 'Gabba'
player['year'] = 2004

print(f"player :{player}")

print("-" * 60)
# delete
print(f"player :{player}")
del player['year']
del player['age']

print(f"player :{player}")
print("-" * 60)
print(dir(player))
