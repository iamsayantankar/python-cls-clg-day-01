a = "12345"

for i in range(1, 6):
    print(" " * (5 - i) + a[:i - 1] + a[i - 1:-6:-1])

for i in range(1, 6):
    print(" " * (5 - i) + a[i - 1:-6:-1] + a[1:i])
