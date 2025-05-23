
import re

ln = "LCNO-MAH-70-2018-9999"

res = re.search(r'LCNO-(KAR|KER|APN|TNS|MAH)-([0-6][1-9]|[1-7][0-3])-([2][0-9]{3})-(?!0000)([0-9]{4})', ln)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found....")
