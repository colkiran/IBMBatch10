
lst1 = list(range(1, 11))
print(f'lst1 :{lst1}')
print("-" * 60)

# iterate through every element of the list
for i in lst1:
    # print(i ** 2, end=" ")
    if i % 2 == 0:
        print(i, end=" ")
print()

print("-" * 60)
# List Comprehension
res = [i for i in lst1]
print(f'res :{res}')

print("-" * 60)
squares = [i ** 2 for i in lst1]
print(f'squares :{squares}')

print("-" * 60)
even_num = [i for i in lst1 if i % 2 == 0]
print(f"Even Numbers :{even_num}")

print("-" * 60)
fruits = [
    ('apple', 385),
    ('orange', 150),
    ('Mango', 90),
    ('pineapple', 75),
    ('gauva', 110),
    ('banana', 80),
    ('pears', 180),
    ('strawberry', 175)
]

print(f"fruits :{fruits}")
print("-" * 60)

price = ["fruit" for fruit in fruits]
print(price)

print("-" * 60)
price = [fruit for fruit in fruits]
print(price)

print("-" * 60)
price = [fruit[0] for fruit in fruits]
print(price)

print("-" * 60)
price = [fruit[1] for fruit in fruits]
print(price)

print("-" * 60)
price = [fruit[1] * 0.9 for fruit in fruits]
print(price)

print("-" * 60)
price = [fruit[1] * 0.75 for fruit in fruits]
print(price)

print("-" * 60)
price = [fruit for fruit in fruits if fruit[1] > 100]
print(price)

print("-" * 60)
exp_frt = [(fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75)
           for fruit in fruits if fruit[1] > 100]
print(exp_frt)

print("-" * 60)
sentence = "the quick brown fox jumps over the lazy dog"
print(sentence)

# iterate through the string
# filter and print the word that is not 'the'
# print all 3 lettered words

print("-" * 60)
res = [word for word in sentence.split()]
print(res)

print("-" * 60)
res  = [word for word in sentence.split() if word != 'the']
print(res)

print("-" * 60)
res = [word for word in sentence.split() if len(word) == 3]
print(res)
