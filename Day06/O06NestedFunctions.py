
def outerFun(info):
    inf = "Mr. " + info
    def innerFun():

        print("Hello World.....")
        print(inf)
        print(info)

    innerFun()

outerFun("Sachin")

