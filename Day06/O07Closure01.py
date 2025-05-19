

def outerFun(info):
    inf = "Mr. " + info
    def innerFun():

        print("Hello World.....")
        print(inf)

    return innerFun

inref = outerFun("Sachin")
# after few lines of code
print("sample text\n" * 5)
inref()

print("-" * 60)
print(outerFun.__name__)
print(outerFun("Sachin").__name__)

print("-" * 60)
outerFun("Rahul")()         # calls the innerFun directly