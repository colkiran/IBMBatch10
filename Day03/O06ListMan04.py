
print("count".center(60, "-"))
lst1 = [1, 2, 1, 2, 3, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]

print(f"1 :{lst1.count(1)}")
print(f"2 :{lst1.count(2)}")
print(f"3 :{lst1.count(3)}")
print(f"5 :{lst1.count(5)}")

print("index".center(60, "-"))
lst1 = [1, 2, 1, 2, 3, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]

print("first index :", lst1.index(3))
print("second index :", lst1.index(3, lst1.index(3) + 1))
print("second index :", lst1.index(3, lst1.index(3, lst1.index(3) + 1) + 1))

print("clear".center(60, "-"))
lst1 = list(range(1, 11))
print(F"lst1 :{lst1}")
lst1.clear()

print(F"lst1 :{lst1}")

print("copy".center(60, "-"))
lst1 = [1, 2, 3, 4, 5]
print(f"lst1 before :{lst1}")

# copy the elements of lst1 to lst2
lst2 = lst1             # shallow copy - copies the address along with the data

print(f"lst2 before :{lst2}")

lst2.append(6)
lst2.append(7)
lst2.append(8)

print(f"lst2 after :{lst2}")
print(f"lst1 after :{lst1}")

print("=" * 60)
print("=" * 60)
print("=" * 60)

lst3 = [10, 20, 30, 40, 50]
print(f"lst3 before :{lst3}")

# copy lst3 to lst4
lst4 = lst3.copy()          # deep copy - where only the data will be copied

print(f"lst4 before :{lst4}")

lst4.extend([60, 70, 80])
print(f"lst4 after :{lst4}")
print(f"lst3 after :{lst3}")

print("=" * 60)
print("=" * 60)
print("=" * 60)

lst5 = [1, 2, 3, [10, 20, 30], 4, 5]
print(f"lst5 before:{lst5}")

# copy lst5 to lst6
lst6 = lst5.copy()
print(f"lst6 before:{lst6}")

lst6[3].append(40)
lst6[3].append(50)
lst6[3].append(60)

print(f'lst6 after :{lst6}')
print(f"lst5 after :{lst5}")

print("=" * 60)
print("=" * 60)
print("=" * 60)

lst7 = [2, 4, 6, [1, 3, 5], 8, 10]
print(f"lst7 before :{lst7}")

# copy lst7 to lst8
from copy import deepcopy
lst8 = deepcopy(lst7)

print(f"lst8 before :{lst8}")

lst8[3].append(7)
lst8[3].append(9)
lst8[3].append(11)

print(f"lst8 after :{lst8}")
print(f"lst7 after :{lst7}")
