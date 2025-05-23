
import time

def fun():
    print("Started executing......")
    time.sleep(2)
    print("Completed executing.......")


st = time.perf_counter()
fun()
fun()
fun()
et = time.perf_counter()
print(f"The total time taken :{round(et - st, 2)}")
