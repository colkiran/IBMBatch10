class CMethod:
    
    teamHead = ""

    @classmethod
    def set_name(cls, name):
       cls.teamHead = name

    @classmethod
    def get_name(cls):
        print(cls.teamHead)

CMethod.set_name("Rohit")
CMethod.get_name()


