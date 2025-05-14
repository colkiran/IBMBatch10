
print("append".center(60, "-"))
lst1 = [1, 2, 3, 4, 5]
print(f"lst1 :{lst1}")

# append
lst1.append(6)
lst1.append(7)
lst1.append(8)

print(f"lst1 :{lst1}")
# lst2 = [10, 20, 30]
# lst1.append(*lst2)

lst1.append([9, 10, 11, 12, 13])

print(f"lst1 :{lst1}")
print(lst1[8][1:4])

print("extend".center(60 ,"-"))
lst2 = [6, 7, 8, 9, 10]
print(f"lst2 :{lst2}")

lst2.extend([11, 12, 13, 14])
print(f'lst2 :{lst2}')

lst2.extend([15])
print(f'lst2 :{lst2}')

print("insert".center(60, "-"))
lst1 = [1, 2, 3, 4, 5]
print(f"lst1 :{lst1}")

lst1.insert(1, 1.5)
lst1.insert(3, 2.5)
lst1.insert(5, 3.5)
lst1.insert(7, 4.5)
print(f"lst1 :{lst1}")

print("pop".center(60, "-"))
lst1 = list(range(1, 11))
print(f"lst1 :{lst1}")

ret = lst1.pop(1)
print(f"ret :{ret}")

ret = lst1.pop(3)
print(f"ret :{ret}")

ret = lst1.pop()
print(f"ret :{ret}")

ret = lst1.pop(-1)
print(f"ret :{ret}")

print(f"lst1 :{lst1}")

print("remove".center(60, "-"))
lst1 = [1, 2, 1, 2, 3, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]

lst1.remove(3)
lst1.remove(3)
lst1.remove(3)

print(f"lst1 :{lst1}")
# remove all 2's from the list

while lst1.count(2):
    lst1.remove(2)

print(f"lst1 :{lst1}")
