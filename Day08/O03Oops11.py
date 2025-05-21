
class Employee:

    def __init__(self, name):
        self.__name = name
        self.tech = ['C++', 'Java', 'J2ee', 'Spring', 'Hibernate', 'Angular JS', 'ReactJS']

    def __str__(self):
        return self.__name + " - " + ", ".join([str(v) for v in self.tech])

emp1 = Employee('Sachin')
print(emp1)
print("-" * 60)

print(emp1.__dict__)
print(emp1._Employee__name)

emp1._Employee__name = "Rahul"
print("-" * 60)

print(emp1.__dict__)
print(emp1._Employee__name)

