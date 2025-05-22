"""
load - is used to read the document from a file
loads - is used to convert JSON string to python dictionary
"""

import json

JFR = open("books.json", "r")
jsonFile = json.load(JFR)

# print(jsonFile['books'])

for book in jsonFile['books']:
    print(book['name'])
    print("-" * len(book['name']))
    for k, v in book.items():
        print(k, "=>", v)
    print("-" * 60)

print("loads".center(60, "-"))
empdata = '{"name": "Kevin", "age": 32, "city": "Los Angels"}'
print(f"empdata :{empdata}")
print(type(empdata))

res = json.loads(empdata)
print(f"res :{res}")
