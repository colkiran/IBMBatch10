
def outerFun():
    gname = "Sachin"
    def innerFun():

        nonlocal gname              # only local var can be converted to nonlocal
        gname += " Tendulkar"
        print("Hello World")
        print(f"Greeting Mr.{gname}")

    innerFun()
    print(f"gname from outerFun :{gname}")

outerFun()
