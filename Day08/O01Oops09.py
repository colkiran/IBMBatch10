
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __add__(self, other):
        return Employee("noName", self.salary + other.salary)

    def __sub__(self, other):
        return Employee("noName", self.salary - other.salary)

    def __mul__(self, other):
        return Employee("noName", self.salary * other.salary)

    def __truediv__(self, other):
        return Employee("noName", self.salary / other.salary)


emp1 = Employee("Jack", 5000)
emp2 = Employee("Slater", 2000)
emp3 = Employee("Kevin", 8000)

print(f"emp1 :{emp1}")
print("-" * 60)

print(f"emp2 :{emp2}")
print("-" * 60)

print(f"emp3 :{emp3}")
print("-" * 60)


# add
print(f"emp1 + emp2 + emp3 = {emp1 + emp2 + emp3}")
print(f"emp3 - emp2 - emp1 = {emp3 - emp2 - emp1}")
print(f"emp1 * emp2 * emp3 = {emp1 * emp2 * emp3}")
print(f"emp3 / emp1 / emp2 = {emp3 / emp1 / emp2}")