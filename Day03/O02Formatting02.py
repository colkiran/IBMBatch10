# conversions
print("Conversions".center(60, "-"))
print("{val} {val} {val}".format(val = "A"))
print("{val!s} {val!r} {val!a}".format(val = "A"))

print("-" * 60)
print("{num} {num} {num}".format(num = 36))
print("{num} {num:f} {num:b}".format(num = 36))
print("{num:10} {num:f} {num:b}".format(num = 36))
print("{num:5} {num:f} {num:b}".format(num = 36))
print("{num:5} {num:f} {num:b}".format(num = 364572344))

print("-" * 60)
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))

print("-" * 60)
from math import pi
print("{pi:10.2}".format(pi=pi))
print("{pi:10.3}".format(pi=pi))
print("{pi:10.4}".format(pi=pi))
print("{pi:10.5}".format(pi=pi))

print("-" * 60)
# Alignment
print("{num:>15} Tendulkar".format(num="Sachin"))      # right alignment
print("{num:^15} Tendulkar".format(num="Sachin"))      # center alignment
print("{num:<15} Tendulkar".format(num="Sachin"))      # left alignment

print("{num:-^60}".format(num = "Sachin Tendulkar"))
print("Sachin Tendulkar".center(60, "-"))

print("{num:010.2}".format(num = pi))
print("{num:010.3}".format(num = pi))
print("{num:010.5}".format(num = pi))

print("-" * 60)
print("{0:10.2f} \n {1:10.2f}".format(pi, -pi))

