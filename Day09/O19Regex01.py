
import re

st = "hello world"
print(f"st :{st}")

# check if the string starts with 'hello'
# match - function, r'' - raw string

res = re.match(r'^hello', st)

print(res)
print(res.group(0))

print("-" * 60)
print(f"st :{st}")

# match works only at the beginning of the string

res = re.search(r'world$', st)
print(res)

print(res.group(0))

print("-" * 60)

st = "the quick brown fox jumps over the lazy dog"
# if st.count("dog"):
if re.search(r'dog', st):
    print(st)




