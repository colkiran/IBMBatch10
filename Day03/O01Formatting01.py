
# emulate printf from C language
format = "Welcome %s, What a %s player"
print(format)
values = ("Sachin", "superb")       # tuple
print(values)

print(format % values)
print("-" * 60)

format = "Welcome %s, your rating of %.3f, what a %s player"
print(format % ("Sachin", 4.7, 'class'))
print(format % ("Sachin", 4.79, 'class'))
print(format % ("Sachin", 4.79032023, 'class'))

print("-" * 60)
print("Welcome %s, your rating of %.3f, what a %s player" % ("Sachin", 4.89345, 'class'))

# emulate Unix shell syntax
from string import Template
tmpl = Template("Welcome $name, what a $adjective player")
print(tmpl)
print(tmpl.substitute(name="Sachin", adjective="superb"))
print("-" * 60)

# format string from python
print("Welcome {}, what a {} player for {}".format("Sachin", "superb", "India"))
print("Welcome {1}, what a {2} player for {0}".format("Sachin", "superb", "India"))
print("Welcome {0}, what a {1} player for {2}".format("Sachin", "superb", "India"))
print("Welcome {pname}, what a {adj} player for {ctry}".format(pname="Sachin", adj="superb", ctry="India"))

print("Welcome {pname}, with a rating of {rating:.3f} what a {adj} player for {ctry}".format(pname="Sachin", adj="superb", ctry="India", rating=4.879345))

print("-" * 60)
# interpolation
from math import pi, e
print(f"PI = pi and Eulers Constant = {e}")

print("PI = {:.3f} and Eulers constant = {:.3f}".format(pi, e))
print("PI = {} and Eulers constant = {} and magic number = {magic}".format(pi, e, magic=40585))

print("-" * 60)
full_name = ['Sachin', 'Tendulkar']
print(f"full_name :{full_name}")
print("Mr.{name}".format(name = full_name))
print("Mr.{name[0]} {name[1]}".format(name = full_name))

print("-" * 60)
import math
print(__name__)         # prints the name of the current module - __main__
print(math.__name__)

print("The {mod.__name__} module gives the value of pi = {mod.pi:.3f} and Eulers constant = {mod.e:.3f}".format(mod=math))
