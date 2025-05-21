"""
r = read mode and it's the default mode

if you open the file in read mode we can only read the contents of the file. we cannot write or append data into the file.

read() - will read all the contents of the file
read(bytes) - will read the data depending on the no of bytes mentioned

readline() - will read one line at a time
readline(bytes) - will read the no of bytes mentioned

readlines() - reads all the lines from the file and stores it in a list
readlines(bytes) - prints the entire line where the byte mentioned falls
"""
FL = open("C:\\Training\\PycharmProjects\\IBMBatch10\\Day08\\data.txt", "r")

# st = FL.read(100)

# st = FL.readline(852)
#
# print(st)

# print(FL.readlines())

for line in FL.readlines(900):
    print(line)

FL.close()