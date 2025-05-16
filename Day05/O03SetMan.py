
s1 = set()
print(f"s1 :{s1}")
print(type(s1))
print("-" * 60)

s2 = {1, 2, 3, 4, 5.2, 6.09, 7.345, 8.9, 9 + 2j, 10 - 3j, 'eleven', 'twelve', 'thirteen', 'fourteen', True, False}
print(f"s2 :{s2}")
print(type(s2))
print("-" * 60)

s3 = set(range(1, 11))
print(f"s3 :{s3}")
print(type(s3))
print("-" * 60)

s1 = set()
# print(f"s1[0] :{s1[0]}")   not subscriptable
# print(dir(s1))
# add values into the set - add, update
print(f"s1 :{s1}")
s1.add(1)
s1.add(2)
s1.add(1)
s1.add(3)
s1.add(1)
s1.add(4)
s1.add(3)
s1.add(5)

print(f"s1 :{s1}")

# update
s1.update([1, 2, 3, 4, 5])
s1.update([4, 5, 6, 7, 1])
s1.update([2, 3, 4, 5, 6])
s1.update([4, 5, 6, 7, 8])
s1.update([3, 4, 5, 6, 7])
s1.update([6, 7, 8, 9, 10])

print(f"s1 :{s1}")
print("-" * 60)

# delete values from the list - pop, remove, discard
print(f"s1 :{s1}")

ret = s1.pop()
print(ret)

ret = s1.pop()
print(ret)

ret = s1.pop()
print(ret)

print(f"s1 :{s1}")
# remove

s1.remove(5)

s1.remove(7)

# s1.remove(1)

print(f"s1 :{s1}")
# discard
s1.discard(4)

s1.discard(8)

s1.discard(1)

print(f"s1 :{s1}")
print("-" * 60)

A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print("-" * 60)
print(f"A union B :{A | B}")
print(f"B union A :{B.union(A)}")

print("-" * 60)
print(f"A intersection B :{A & B}")
print(f"B intersection A :{B.intersection(A)}")

print("-" * 60)
print(f"A difference B :{A - B}")
print(f"B difference A :{B.difference(A)}")

print("-" * 60)
print(f"A symmetric_difference B :{A ^ B}")
print(f"B symmetric_difference A :{B.symmetric_difference(A)}")

print("-" * 60)
# frozenset - are immutable
fset = frozenset([1, 2, 3, 4, 5])
print(f"fset :{fset}")
print(type(fset))

print("-" * 60)
s1 = {(1, 2, 3), (4, 5, 6), (7, 8, 9)}
print(f's1 :{s1}')
print(type(s1))
