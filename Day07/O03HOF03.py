import time


def funlogger(fnc):
    def helper():
        print("My info logged into a service......")
        fnc()
        print("My info logged out of the service.....")

    return helper

def normal_fun():
    print("I should be called normal......")

funlogger(normal_fun)       # no output
print("-" * 60)

funlogger(normal_fun)()
print("-" * 60)

res_fun = funlogger(normal_fun)
res_fun()

print("-" * 60)
normal_fun = funlogger(normal_fun)
normal_fun()            # calls the helperFun

print("-" * 60)

@funlogger      # basicFun = funlogger(basicFun)
def basicFun():
    print("I should be called basic......")

# basicFun = funlogger(basicFun)
basicFun()

