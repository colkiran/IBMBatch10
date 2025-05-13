
st = "hello world"
print(f"st :{st}")
print(type(st))

# print(st.upper())
print("-" * 60)
print(f"st :{st}")
print(f"st[0] :{st[0]}")
print(f"st[6] :{st[6]}")
print(f"st[10] :{st[10]}")

print("-" * 60)
# slicing - pull a part of the string using their indexes
print(f"st[0:5] :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[0:11:2] :{st[0:11:2]}")
print(f"st[0:]     :{st[0:]}")
print(f"st[:11]    :{st[:11]}")
print(f"st[:]      :{st[:]}")

# reverse indexing
print("-" * 60)
print(f"st[-1] :{st[-1]}")
print(f"st[-5] :{st[-5]}")
print(f"st[-11] :{st[-11]}")

# slicing
print("-" * 60)
print(f"st[-1:-6:-1]  :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[::-1]      :{st[::-1]}")

print("-" * 60)
# code to find if a string is a palindrome
st = "malayalam"
print("palindrome" if st[:] == st[::-1] else "Not a palindrome")

print("-" * 60)
# strings are immutable (does not have a setter method)
st = "hello"
print(f"st :{st}")
print(f"st[0] :{st[0]}")
# st[0] = "H"

print("-" * 60)
st = "****hello*********"
print(f"st :{st}")

res = st.lstrip("*")
print(f"res :{res}")

res = st.rstrip("*")
print(f"res :{res}")

res = st.strip("*")
print(f"res :{res}")

print("-" * 60)
st = "hello"
print(f"st :{st}")


# def replace(s):   # hello
#     return (s.capitalize())
#
# st = "hello"
# print(replace(st))


res = st.replace("h", "H")
print(f"res :{res}")

print("maketrans".center(60, "-"))
st = "hello world"
print(f"st :{st}")
a = "helowrd"
b = "HELOWRD"
# the length of a and b should be the same
resTbl = st.maketrans(a, b)
print("resTbl :", resTbl)

print("translate".center(60, "-"))
res = st.translate(resTbl)
print(f"res :{res}")
