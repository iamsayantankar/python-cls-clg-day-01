a = "12345"

for i in range(1, 6):
    print(" " * (5 - i) + a[:i - 1] + a[i - 1:-6:-1])

for i in range(1, 6):
    print(" " * (5 - i) + a[i - 1:-6:-1] + a[1:i])

for i in range(1, 6):
    print(" " * (5 - i) + a[i - 1:-6:-1] + a[1:i])

for i in range(1, 6):
    if i == 1 or i == 5:
        print(a[:i])

    else:
        print(a[0], end="")
        print(" " * (i - 1), end="")
        print(a[i - 1])
