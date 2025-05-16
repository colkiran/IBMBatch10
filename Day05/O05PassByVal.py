# pass by values goes with immutable data

def fun(x):
    print(f"x before:{x}")
    x += 50
    print(f"x after :{x}")

y = 100
print(f"y before call :{y}")
fun(y)
print(f"y after call :{y}")
