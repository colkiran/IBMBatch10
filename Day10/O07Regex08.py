
import re


# [] - character class
"""
between b and t there should be only vowels
res = re.search(r'b[aeiou]t', st)
"""

"""
between b and t there should not be vowels
res = re.search(r'b[^aeiou]t', st)
"""

st = 'b6t'
"""
between b and t there should be alphabets (lower case), (upper case), number
"""
res = re.search(r'b[a-zA-Z0-9]t', st)


if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found....")


