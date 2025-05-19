
def greet():
    print("Greetings Mr.Sachin Welcome to the event......")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event......")


# city is called default arg, gname is called non default arg
def greetGstCty(gname, city = "Mumbai"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event.......")

greet()
print('-' * 60)

greetGst("Virat")
greetGst("Rohit")

print('-' * 60)
greetGstCty("Sachin")
greetGstCty("Rohit")
greetGstCty("Rahul", "Bangalore")

print('-' * 60)
def admsn(fname, lname, dob, qlf, gender, conno, city, marital_sts, emialid):
    print(f"Name :{fname + " " + lname}")
    print(f"DOB  :{dob}")
    print(f"Qualification :{qlf}")
    print(f"gender :{gender}")
    print(f"Contact No.", {conno})
    print(f"City :{city}")
    print(f"Marital Status :{marital_sts}")
    print(f"Email ID :{emialid}")

# args
admsn("John", 'Salter', '12/10/1983', 'Science Graduate', 'Male', '282343453', 'Philadelphia', "Married",
      'john@gamail.com' )

print('-' * 60)
# kwargs
admsn(qlf = "Engineering Graduate", emialid='Kevin@gmail.com', gender='Male', marital_sts='Single', dob='15/01/2002',
      city = 'Denver', conno="9902380923", fname="Kevin", lname='Richard')

print('-' * 60)
# variable length arguments - *args, **kwargs

def ProdAll(*numbers):
    print(*numbers)         # unpacking
    print(numbers)
    prod = 1
    for num in numbers:
        prod *= num
    return prod

print(ProdAll(1, 2, 3, 4, 5))

print("-" * 60)

def extractDetails(**details):
    print(details)
    for k, v in details.items():
        print(k, '=>', v)

extractDetails(name='Kennedy', age=35, dept="Finance", desig="MGR", city="California")

print("-" * 60)
def multiply_me(x, y):
    return x * y

a = 45
b = 7
print(f"The product of {a} and {b} is :{multiply_me(a, b)}")

print("-" * 60)
# function can return more than one value

def ArithCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = ArithCalc(20, 8)
print(f"res :{res}")

print("-" * 60)

# recursive calls - function calling itself

# factorial of a number, fibonacci series
def factorial(x):
    if (x == 1):
        return 1
    else:
        return x * factorial(x - 1)


print(f"The factorial of 4 is :{factorial(4)}")

print("-" * 60)
def fibo(x):
    if x == 0 or x == 1:
        return x
    else:
        return fibo(x - 1) + fibo(x - 2)


iter = int(input("Enter the number of fibonnaci numbers to be generated :"))
for i in range(iter):
    print(fibo(i), end=" ")
print()

print("-" * 60)
# docstrings - they are written on top of functions which specifies the information about the function

def fun():
    # this is a comment
    "this is a docstring"
    print("Hello World")

fun()
print(fun.__doc__)

print("-" * 60)

def fun1(x, y):
    """
    funtion fun1
    ------------
    1. if we pass both the arguments as strings then the result will be a concatenated string
    2. if we pass two numbers then the result will be the sum of the numbers
    3. if we pass a number and a string then the result will be an error
    """
    return x + y

print(fun1("hello", " world"))
print(fun1(64, 26))
# print(fun1(10, "hello"))

print("-" * 60)
help(fun1)
