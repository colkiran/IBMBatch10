"""
FA = open(filename + path, "a")

if the file already exists then it will append the new data into the file without disturbing the existing contents.

if the file does not exist then creates a new file and then writes it into the file.
"""

FA = open("myfile.txt", "a")

st = input("Enter the contents of the file :")
FA.write(st + "\n")

FA.close()