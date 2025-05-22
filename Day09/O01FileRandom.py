
FL = open("data.txt", 'rb')

# tell returns the position of the file handle
print(FL.tell())

pos = FL.seek(150, 0)
print(f"position :{pos}")

pos = FL.seek(-85, 1)
print(f"position :{pos}")

pos = FL.seek(50, 2)
print(f"position :{pos}")

# pos = FL.seek(-10, 0)
# print(f"position :{pos}")

pos = FL.seek(-50, 2)
print(f"position :{pos}")

FL.close()