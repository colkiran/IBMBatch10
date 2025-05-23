import json

import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "getproduct/pepsi")

# print(response)
res = response.json()

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)

print("PUT".center(60, "-"))

response = requests.put(BASE + "getproduct/coke", data={'cat': 'baverage'})
res = response.json()

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)

print("PATCH".center(60, "-"))
data = {'price': 5000}
response = requests.patch(BASE + "getproduct/coke", json=json.dumps(data))
res = response.json()

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)

print("POST".center(60, "-"))
fanta = {'item': '200 ml bottle', 'price': 20, 'qty': 400}

response = requests.post(BASE + "getproduct/fanta", json=json.dumps(fanta))
res = response.json()

for k, info in res.items():
    print(k)
    print("-" * len(k))
    for k,v in info.items():
        print(k, "=>", v)

print("DELETE".center(60, "-"))

response = requests.delete(BASE + "getproduct/Thumbs_up")
res = response.json()

for k, info in res.items():
    print(k)
    print("-" * len(k))
    for k,v in info.items():
        print(k, "=>", v)