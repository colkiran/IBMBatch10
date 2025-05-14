
values = list(range(10, 31, 10))
print(f"values :{values}")

# unpack the list
a, b, c = values
print(a, b, c, sep=", ")

print("-" * 60)
values = list(range(10, 101, 10))
print(f"values :{values}")

a, b, *c = values           # var with a * can store more than one value
print(f"a = {a}, b = {b}, c = {c}")

a, *b, c = values
print(f"a = {a}, b = {b}, c = {c}")

*a, b, c = values
print(f"a = {a}, b = {b}, c = {c}")

print("-" * 60)
lst1 = [1, 2, 3, 4, 5]
lst2 = [11, 22, 33, 44, 55]

lst3 = [lst1, lst2]
print(f"lst3 :{lst3}")
print(len(lst3))

lst4 = [*lst1, *lst2]
print(f"lst4 :{lst4}")
print(len(lst4))

print("-" * 60)

letters = ['a', 'b', 'c', 'd', 'e']
print(f"letters :{letters}")

for letter in letters:
    print(letter, end=" ")
print()

print("-" * 60)
for letter in enumerate(letters):
    print(letter, end=" ")
print()

print("-" * 60)
for letter in enumerate(letters):
    print(letter[0], letter[1])

print("-" * 60)
for index, letter in enumerate(letters):
    print(index, letter)

print("-" * 60)
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"mylist :{mylist}")

print("-" * 60)
for list in mylist:
    print(list)

print("-" * 60)
for ind, lst in enumerate(mylist):
    print(f"{ind} \t {lst}")

print("-" * 60)
for ind, lst in enumerate(mylist):
    print(f'List({ind})')
    for idx, val in enumerate(lst):
        print(f"\t{idx}\t{val}")

print("-" * 60)
print(dir(lst1))

