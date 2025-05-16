
t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))
print("-" * 60)

t2 = (1, 2, 3, 4.5, 5.08, 6.0, 7 + 3j, 8 - 0j, True, False, 'eleven', 'twelve')
print(f"t2 :{t2}")
print(type(t2))
print("-" * 60)

t3 = tuple(range(1, 11))
print(f"t3 :{t3}")
print(type(t3))
print("-" * 60)

t4 = 1,
print(f"t4 :{t4}")
print(type(t4))
print("-" * 60)

t5 = 1, 2, 3, 4, 5
print(f"t5 :{t5}")
print(type(t5))
print("-" * 60)

t1 = (1, 2, 3, 4, 5)
print(f"t1 :{t1}")

# it is immutable
# print(t1[1])
# t1[1] = 500
l1 = list(t1)
print(f"l1 :{l1}")
print(type(l1))

l1.extend([6, 7, 8, 9, 10])
print(f"l1 :{l1}")
t1 = tuple(l1)
print(f"t1 :{t1}")
print(type(t1))

print('count'.center(60, "-"))
t1 = (1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1)
print(f"t1 :{t1}")

print("-" * 60)
print(f"1 :{t1.count(1)}")
print(f"2 :{t1.count(2)}")
print(f"3 :{t1.count(3)}")
print(f"5 :{t1.count(5)}")

print("index".center(60, "-"))
print(f"t1 :{t1}")

print("-" * 60)
print(f"First index of 3  :{t1.index(3)}")
print(f"Second index of 3 :{t1.index(3, t1.index(3) + 1)}")
print(f"Third index of 3  :{t1.index(3 , t1.index(3, t1.index(3) + 1) + 1)}")


