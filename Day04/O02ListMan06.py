
lst1 = [1, 2, 3, 4, 5]
lst2 = [11, 22, 33, 44, 55]

print(zip(lst1, lst2))
print(list(zip(lst1, lst2)))

print("-" * 60)
lst1 = [1, 2, 3, 4]
lst2 = [11, 22, 33, 44, 55]
print(list(zip(lst1, lst2)))

print("-" * 60)
lst1 = [1, 2, 3, 4, 5]
lst2 = [11, 22, 33, 44]
print(list(zip(lst1, lst2)))

print("-" * 60)
lst1 = [1, 2, 3, 4, 5]
lst2 = [11, 22, 44, 55]

print(list(zip("abcde", lst1, lst2)))
print(list(zip("ab", lst1, lst2)))
