
def fun(*args):
    print(*args)
    print(args)
    print("-" * 60)

fun()
fun(1)
fun(1, 2)
fun(1, 2, 3)
fun(1, 2, 3, 4)

print("-" * 60)

def sum(x, y):
    print("sum func called.....")
    return x + y

def diff(x, y):
    print("diff func called.....")
    return x - y


def log_details(fnc):
    logInfo = "Logging into the service...."

    def innerFun(*args):
        print(logInfo)
        print(fnc(*args))
        print("-" * 60)

    return innerFun

a = log_details(sum)
print(type(a),"\t",  a.__name__)
a(35, 74)

diffLogger = log_details(diff)
diffLogger(30, 12)
