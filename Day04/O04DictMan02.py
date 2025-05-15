
print("keys".center(60, "-"))
player = {'name': 'Sachin', 'age': 35, 'runs': 89, 'oppn': 'Aus'}
print(f"player :{player}")

ky = player.keys()
print(f'Keys :{ky}')

print("-" * 60)
for k in player.keys():
    print(k + " => " + str(player[k]))

print("values".center(60,"-"))
player = {'name': 'Sachin', 'age': 35, 'runs': 89, 'oppn': 'Aus'}
print(f"player :{player}")

vl = player.values()
print(f"values :{vl}")

print("items".center(60, "-"))
# items = keys + values
emp = {
    'emp1': {'empid': 'EMP111', 'name': 'Peter', 'age': 32, 'desig': 'TL', 'dept': 'Finance', 'sal': 95000},
    'emp2': {'empid': 'EMP212', 'name': 'Tina', 'age': 38, 'desig': 'MGR', 'dept': 'Admin', 'sal': 125000},
    'emp3': {'empid': 'EMP339', 'name': 'Richard', 'age': 29, 'desig': 'SE', 'dept': 'IT', 'sal': 80000}
}

print(f"emp :{emp}")
print("-" * 60)

print(f"emp1 :{emp['emp1']}")

print("-" * 60)
print(f"emp2 :{emp['emp2']}")

print("-" * 60)
print(f"emp3 :{emp['emp3']}")

print("-" * 60)
for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)

print("get".center(60, "-"))
emp1  = {'empid': 'EMP111', 'name': 'Peter', 'age': 32, 'desig': 'TL', 'dept': 'Finance', 'sal': 95000}
print(f"emp1 :{emp1}")

print(f"Name  :{emp1.get('name', 'Invalid key please enter a valid key.....')}")
print(f"Desig :{emp1.get('desg', 'Invalid key please enter a valid key.....')}")

print("fromkeys".center(60, "-"))
# convert a list into a dictionary
cities = ['blr', 'che', 'del', 'mum', 'hyd', 'kol']
print(f"cities :{cities}")
print(type(cities))

res1 = dict.fromkeys(cities)
print(f"res1 :{res1}")

res1 = dict.fromkeys(cities, 24)
print(f"res1 :{res1}")

print("setdefault".center(60, "-"))
# used to add new key value pairs
emp2 = {'empid': 'EMP212', 'name': 'Tina', 'age': 38, 'desig': 'MGR', 'dept': 'Admin', 'sal': 125000}
print(f"emp2 :{emp2}")

emp2.setdefault('name', 'Mary')
emp2.setdefault('desig', 'GM')

emp2.setdefault('city', 'California')
emp2.setdefault('ConNo', '2834728397')

print(f"emp2 :{emp2}")
