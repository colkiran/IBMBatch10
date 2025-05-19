# def outerFun(greet, flag):
def outerFun(greet):
    def innerFun(gname):

        print(greet, gname)

    return innerFun
    # if flag:
    #     return innerFun1
    # else:
    #     return innerFun2

outerFun("Welcome")("Sachin")

# simple curry
engGrt = outerFun("Welcome")
kanGrt = outerFun("Namaskara")

print("-" * 60)
engGrt("Sachin")

print("-" * 60)
kanGrt("Rahul")

#------------------------------------
def outerFun(greet):

    def innerFun(gname):

        print(greet, gname)

    return innerFun

inref = outerFun("Welcome")
inref("Virat")

# inref = innerfun
# inref()