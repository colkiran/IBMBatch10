
for i in range(1, 11):
    print(i, end=" ")
print()

print("-" * 60)
for i in range(10):
    print(f"hello world :{i}")

print("-" * 60)
for i in range(1, 31):
    # if i > 25:
    #     break               # stop the iteration
    if i % 2 == 1:
        continue            # skip the iteration
    else:
        print(i, end=" ")
else:
    print("\nCompleted generation of numbers......")