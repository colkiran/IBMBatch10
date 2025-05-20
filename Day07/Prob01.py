
import time
def timeCalc(fnc):
    def helper(tm):
        print("Function called.....")
        st = time.perf_counter()
        fnc(tm)
        et = time.perf_counter()
        print("Completed execution....")
        print(f"The total time taken by the function to execute :{round(et - st, 2)}")
    return helper

@timeCalc
def fun(x):
    lst = []
    for i in range(x):
        for j in range(1, x + 1):
            lst.append(j ** 3)

print(fun.__name__)
fun(6500)