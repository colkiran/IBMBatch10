
emp1  = {'empid': 'EMP339', 'name': 'Richard', 'age': 29, 'dept': 'IT', 'sal': 95000, 'desig': 'SE'}

print("-" * 60)
print(f"emp1 :{emp1}")

print("-" * 60)
# for i in emp1.keys():
# for i in emp1.values():
for k, v in emp1.items():
    print(k, "=>", v)
    # print(i, end=" ")
# print()

print("-" * 60)
res = [x for x in emp1]
print(f"res :{res}")

print("-" * 60)
res = [x for x in emp1.keys()]
print(f"res :{res}")

print("-" * 60)
res = [x for x in emp1.values()]
print(f"res :{res}")

print("-" * 60)
res = [(k, v) for k, v in emp1.items()]
print(f"res :{res}")
