
globX = 100

def fun(x):             # x is a local varible
    global globX        # do not assign any value in this line
    print(f'x :{x}')
    globX = 500
    print(f"globX inside function :{globX}")


print(f"globX before function call :{globX}")

fun(10)

print(f"globX after function call  :{globX}")
