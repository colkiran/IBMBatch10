def callMe():
    print("Apples from Ooty")

def fun(fnc):
    print("Hello".center(60, "-"))
    fnc()
    print("Hi".center(60,"-"))
    print("-" * 60)

    def defieneMe():
        print("Oranges from Kanpur......")

    return defieneMe

def funCallBack(fnc):
    print("Mera Bharath Mahan".center(60, "-"))
    fnc()
    print("India is great".center(60, "-"))

funCallBack(fun(callMe))
