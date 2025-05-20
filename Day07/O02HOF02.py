
def greet(msg):
    print(msg)

greet("Welcome")
fun_name = greet

print(fun_name.__name__)
print(greet.__name__)

fun_name("Hello")

print("-" * 60)

def bank_flow(fnc, x):     # HOF
    print("Login".center(60, "-"))
    print(fnc(x))               # call back
    print("Logout".center(60,"-"))


def deposit(amt):
    return f"Amount {amt} Credited into the account....."

def withdraw(amt):
    return f"Amount {amt} Debited from the account......."

print("-" * 60)

bank_flow(deposit, 1000)

print("-" * 60)

bank_flow(withdraw, 500)