
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 60)
l2 = [1, 2, 3, 4, 5,1, 6.2, 7.9, 8.0, 'nine', 'ten', 'eleven', 'twelve', 13 + 2j, 14 - 5j, True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 60)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 60)
# CRUD
# Create
lst1 = [1, 2, 3, 4, 5]
print(f"lst1 :{lst1}")

print("-" * 60)
# read
print(f"lst1 :{lst1}")
print(f"lst1[1] :{lst1[1]}")
print(f"lst1[3] :{lst1[3]}")
print(f"lst1[-1] :{lst1[-1]}")

for i in lst1:
    print(i, end=" ")
print()

print("-" * 60)
# Update  = 1. modify the existing values, 2. add a new value to the list

# modify
print(f"lst1 :{lst1}")
lst1[2] = 300
lst1[-1] = 500
print(f"lst1 :{lst1}")

# adding a new value
lst1[3] = 301
print(f"lst1 :{lst1}")

# list in python is static, so we cannot add new values into the list manually

print("-" * 60)
# Delete
print(f"lst1 :{lst1}")
del lst1[1]
del lst1[-1]

print(f"lst1 :{lst1}")
