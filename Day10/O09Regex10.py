
import re

st = 'sample.py'

# . - single character
# \ - to supress the regex

res = re.search(r'\.py$', st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found....")


