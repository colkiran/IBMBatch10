
"""
sort  - will sort the original array
sorted - will take a copy of the array and then sort it
"""
lst1 = [9, 3, 4, 10, 8, 1, 5, 2, 6, 7]
print(f"lst1 :{lst1}")

res_asc = sorted(lst1)
res_desc = sorted(lst1, reverse=True)

print(f"res_asc :{res_asc}")
print(f"res_desc :{res_desc}")

print("-" * 60)
lst1 = [9, 'zebra', 'apple', 3,'yellow', 'blue', 4, 'white', 'green', 10, 'orange', 'pink', 8, 'egg', 'xray', 1, 'violet', 'magenta', 5, 'hen', 2, 6, 7, 198, 1045, 29, 265, 2134]
print(f"lst1 :{lst1}")

print("-" * 60)
res_asc = sorted(lst1, key=ascii)
print(f"res_asc :{res_asc}")

# print("-" * 60)
index = []
for num in res_asc:
    if type(num) == int:
        index.append(res_asc.index(num))

# print(index)
# index = [res_asc.index(num) for num in res_asc if type(num) == int]
# [res_asc.index(num) for num in res_asc if type(num) == int] - list comprehension
# print(index)

print("-" * 60)
print(res_asc[:index[0]]+ sorted(res_asc[index[0]:]) )

print("-" * 60)
cities = ['ooty', 'thiruvananthapuram', 'delhi', 'bangalore', 'chennai', 'mumbai', 'pune', 'vishakapatnam', 'hyderabad', 'kolkata']

# sort these cities by the length (no of characters)

cities_sort=sorted(cities,key=len)
print(cities_sort)



