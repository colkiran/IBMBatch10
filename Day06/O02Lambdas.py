
def sum(x, y):
    return x + y

a = sum
res = a(100, 200)
print(f"res :{res}")

print("-" * 60)
# b = lambda x, y : a(x, y)
b = lambda x, y : x + y

res = b(43, 82)
print(f"res :{res}")

print("-" * 60)
# lambdas are best used with map, filter and reduce

# map - expression if lambda will be implemented on all arguments passed to it - (x - (x * 0.1))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

squares = list(map(lambda x : x ** 2, l1))
print(f"squares :{squares}")

# conversions - kgs to pounds, currency, litres to gallons
months = ['dec', 'sep', 'aug', 'feb', 'nov', 'oct', 'jan', 'mar', 'jun', 'apr', 'jul', 'may']
print(f"months :{months}")

print("-" * 60)
# sort these months same as calendar months
from calendar import month_abbr
print(list(month_abbr))

print("-" * 60)
sorted_months = sorted(months, key=list(map(lambda mth : mth.lower(), list(month_abbr))).index)
print(f"sorted_months :{sorted_months}")

print("-" * 60)
# filter - expression will return a True or a False
l1 = list(range(1, 31))
print(f"l1 :{l1}")

print("-" * 60)
res = list(filter(lambda x : x % 3 == 0, l1))
print(f"res :{res}")

print("-" * 60)
sentence = "the quick brown fox jumps over the lazy dog."
print(f"sentence :{sentence}")
res = list(filter(lambda x : x != 'the', sentence.split()))
print(f"res :{res}")

print("-" * 60)
# reduce - reduces the list into a single element
from functools import reduce
l1 = [8, 4, 1, 5, 9, 7, 6, 10, 2, 3]
print(f"l1 :{l1}")

res = reduce(lambda x, y : x if x > y else y, l1)
print(f"Largest :{res}")

res = reduce(lambda x, y : x if x < y else y, l1)
print(f"Smallest :{res}")

res = reduce(lambda x, y : x + y, l1)
print(f"Sum :{res}")

