
import re

st = 'baaaaaaat'

# {3,7}   - min 3 and max 7 times
res = re.search(r'ba{3,7}t', st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found....")


