
for i in range(5, 0, -1):
    for k in range(1, 6-i):
        print(" ", end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()

for i in range(2,6):
    for k in range(5-i, 0, -1):
        print(" ", end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

print("-" * 60)

st = "The scores are {scr} after 20 overs"
print(st.format(scr=145))

st = "The run rate after after 20 overs {rnrt:.2f}"
print(st.format(rnrt = 7.896355))

