# any variable declared inside a function is not accessible outside the function - lexical - only accessible inside a block of code

def fun(x):         # x is a local variable
    print(f"x :{x}")
    y = "Hello World"       # y is a local variable
    print(f"y :{y}")

fun(10)

print("-" * 60)
# print(f"x outside the function :{x}")
# print(f"y outside the function :{y}")