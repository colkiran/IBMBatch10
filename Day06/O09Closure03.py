# HOF = Higher Order Function
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(gname):

            from emojis import emojis

            emojized = emojis.encode(greet + " :" + sep + ": " + gname)

            print(emojized)

        return innerMostFun

    return innerFun


KanGrt = outerFun("Namaskara")

tgrKanGrt = KanGrt("tiger")
lnKanGrt = KanGrt("lion")

tgrKanGrt("Prabhakar")
lnKanGrt("Vishnuvardhan")



"""

engGrt = outerFun("Welcome")        # innerFun


engGrtSngArw = engGrt("------>")    # innerMostFun
engGrtDblArw = engGrt("=====>>")

engGrtSngArw("Sachin")
engGrtDblArw("Rohit")
"""