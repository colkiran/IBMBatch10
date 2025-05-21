import time


class TimeCalculator:

    def __init__(self, fnc):
        self.fnc = fnc

    def __call__(self, *args, **kwargs):
        print("Execution Started.......")
        st = time.perf_counter()
        res = self.fnc(*args, **kwargs)
        et = time.perf_counter()
        print("Execution completed.....")
        print(f"The total time take by the function to get executed :{round(et - st, 2)}")
        return res

@TimeCalculator
def fun(n):
    lst = []
    for i in range(n):
        for j in range(1, i + 1):
            lst.append(j ** 3)


fun(6500)