"""
open(filename + path, "w")

writemode => if the file already exists then it will overwrite the contents into the existing file.
if the file does not exist then creates a new file and write into the file.

write - writes one line at a time

writelines - writes multiple lines
"""

FW = open("myfile.txt", "w")
# st = input("Enter the contents of the file :")
# FW.write(st)

l1 = "This is the first line.\n"
l2 = "This is the second line.\n"
l3 = "This is the third line.\n"

FW.writelines([l1, l2, l3])

FW.close()