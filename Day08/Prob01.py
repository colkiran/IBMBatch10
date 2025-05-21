
class Test:

    def fun(self, *args):
        print(args)




t1 = Test()
t1.fun()
t1.fun(1)
t1.fun(1, 2)
t1.fun(1, 2, 3)
