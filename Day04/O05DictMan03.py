
print("pop".center(60, "-"))
emp2 = {'empid': 'EMP212', 'name': 'Tina', 'age': 38, 'desig': 'MGR', 'dept': 'Admin', 'sal': 125000}

print(f"emp2 :{emp2}")
ret = emp2.pop('age')
print(f"ret :{ret}")

ret = emp2.pop('dept')
print(f"ret :{ret}")

# ret = emp2.pop()
# print(f"ret :{ret}")


print(f"emp2 :{emp2}")

print("popitem".center(60, "-"))
emp2 = {'empid': 'EMP212', 'name': 'Tina', 'age': 38, 'desig': 'MGR', 'dept': 'Admin', 'sal': 125000}
print(f"emp2 :{emp2}")

ret = emp2.popitem()
print(f"ret :{ret}")

ret = emp2.popitem()
print(f"ret :{ret}")

ret = emp2.popitem()
print(f"ret :{ret}")

print(f"emp2 :{emp2}")

print("update".center(60, "-"))
emp1 = {'empid': 'EMP111', 'name': 'Peter', 'age': 32, 'dept': 'Finance', 'sal': 95000}

emp3 = {'empid': 'EMP339', 'name': 'Richard', 'age': 29, 'desig': 'SE', 'dept': 'IT'}

print(f"emp1: {emp1}")
print(type(emp1))

print("-" * 60)
print(f"emp3 :{emp3}")
print(type(emp3))

print("-" * 60)
emp1.update(emp3)

print(f"emp1 :{emp1}")

print("copy".center(60, "-"))
emp1 = {'empid': 'EMP339', 'name': 'Richard', 'age': 29, 'desig': 'SE', 'dept': 'IT'}
print(f"emp1 before :{emp1}")

print("-" * 60)
# copy emp1 into emp2
emp2 = emp1         # shallow copy
print(f'emp2 before :{emp2}')

print("-" * 60)
emp2['sal'] = 125000
emp2['city'] = 'LA'
print(f"emp2 after :{emp2}")
print(f"emp1 after :{emp1}")

print("-" * 60)
print("-" * 60)

emp3 = {'empid': 'EMP111', 'name': 'Peter', 'age': 32, 'dept': 'Finance', 'sal': 95000}
print(f"emp3 before :{emp3}")
print("-" * 60)

# copy emp3 to emp4
emp4 = emp3.copy()          # deep copy
print(f"emp4 before :{emp4}")

print("-" * 60)
emp4['desig'] = 'TL'
emp4['city'] = 'NYK'

print(f"emp4 after :{emp4}")
print(f"emp3 after :{emp3}")

print("-" * 60)
print("-" * 60)

emp5 = {'empid': 'EMP111', 'name': 'Peter', 'age': 32, 'dept': 'Finance', 'sal': 95000, 'desig' : {'HP': 'FE','TCS': 'FL'}}
print(f"emp5 before :{emp5}")

print("-" * 60)
# copy emp5 to emp6
emp6 = emp5.copy()
print(f"emp6 before :{emp6}")
print("-" * 60)
emp6['desig']['dell'] = 'MGR'
emp6['desig']['tesco'] = 'SMGR'

print(f"emp6 after :{emp6}")
print("-" * 60)
print(f"emp5 after :{emp5}")

print("-" * 60)
print("-" * 60)

emp7 = {'empid': 'EMP111', 'name': 'Peter', 'age': 32, 'dept': 'Finance', 'sal': 95000, 'desig' : {'HP': 'FE', 'TCS': 'FL'}}
print(f"emp7 before :{emp7}")

# copy emp7 to emp8
from copy import deepcopy
emp8 = deepcopy(emp7)
print("-" * 60)
print(f"emp8 before :{emp8}")
print("-" * 60)
emp8['desig']['dell'] = 'MGR'
emp8['desig']['tesco'] = 'SMGR'

print(f"emp8 after :{emp8}")
print("-" * 60)
print(f"emp7 after :{emp7}")
