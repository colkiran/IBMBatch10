
import re

st = 'baaat'

# 3   - exactly 3 times
res = re.search(r'ba{3}t', st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found....")


