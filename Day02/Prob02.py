cntr = 0
for n in range(50, 150+1):
   for m in range(2,n):
       if n % m == 0:
           break
   else:
    print(n, end=" ")
    cntr += 1

print(f"\nThere are {cntr} prime numbers between 150 and 50")