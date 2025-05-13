def x():
    count = 1
    row = 1
    while (count < 10):
        for j in range(row):
            print(count - 1, end=" ")
            count += 1
        row += 1

        print()


x()