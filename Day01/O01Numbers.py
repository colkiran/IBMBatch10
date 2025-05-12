
"""
1. integer
2. float
3. complex
"""

a = 10
b = -10
print(f"a :{a}")
# 'a' is an object class integer
print(type(a))          # RTTI - Runtime type identification
print(f"b :{b}")
print(type(b))

print("-" * 60)
c = 10.0
d = -10.0
print(f"c :{c}")
print(type(c))
print(f"d :{d}")
print(type(d))

print("-" * 60)
e = +2e3        # 2 * 1000.0
f = -2e3        # -2 * 1000.0
print(f"e :{e}")
print(type(e))
print(f"f :{f}")
print(type(f))

print("-" * 60)
g = 3.14j
h = -3.14j

print(f"g :{g}")
print(type(g))
print(f"h :{h}")
print(type(h))

print("-" * 60)
print(max(10, 17, 14))
print(min(10, 17, 14))

print("-" * 60)
x = 2 + 3.5
print(f"x :{x}")
print(type(x))

print("-" * 60)
x = 2
y = 3.5
z = x + y
print(f"x = {type(x)}")
print(f"y = {type(y)}")
print(f"z = {type(z)}")

print("Conversion".center(60, "-"))
a = 100
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
# a = 0 => false
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number System".center(60, "-"))
print(f"11    :{11}")          # decimal numbers
print(f"0b11  :{0b11}")        # binary
print(f"0b101 :{0b101}")       # binary
print(f"0o11  :{0o11}")        # octal
print(f"0o101 :{0o101}")       # octal
print(f"0o15  :{0o15}")        # octal
print(f"0xe   :{0xe}")         # hexa
print(f"0xa   :{0xa}")         # hexa

print("Number System Conversion".center(60, "-"))
a = 100
print(f"a :{a}")
print(f"bin(a) :{bin(a)}")
print(f"oct(a) :{oct(a)}")
print(f"hex(a) :{hex(a)}")
