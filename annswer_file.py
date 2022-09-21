
for i in range(1, 6):
    print("*" * i)

for i in range(5, 0, -1):
    print("*" * i)

for i in range(1, 6):
    print(" " * (5 - i) + "*" * i)

for i in range(5, 0, -1):
    print(" " * (5 - i) + "*" * i)

for i in range(1, 6):
    print(" " * (5 - i), end="")
    print("*" * (i * 2 - 1))

for i in range(1, 10):
    if i > 5:
        print(" " * (5 - i), end="")
        print("*" * (10 - i))
    else:
        print(" " * (5 - i) + "*" * i)

for i in range(1, 10):
    if i > 5:
        print(" " * (i - 5), end="")
        print("*" * (10 - i))
    else:
        print(" " * (5 - i) + "*" * i)

for i in range(1, 10):
    if i > 5:
        print(" " * (i - 5), end="")
        print("*" * (2 * (10 - i) - 1))
    else:
        print(" " * (5 - i), end="")
        print("*" * (i * 2 - 1))

for i in range(1, 10):
    if i < 6:
        print("*" * (6 - i), " " * (i * 2 - 1), "*" * (6 - i))
    else:
        print("*" * (i - 4), " " * (2 * (10 - i) - 1), "*" * (i - 4))

for i in range(1, 10):
    if i < 6:
        print("*" * (6 - i), end="")
        print(" " * (i * 2 - 2), end="")
        print("*" * (6 - i))
    else:
        print("*" * (i - 4), end="")
        print(" " * (2 * (10 - i) - 2), end="")
        print("*" * (i - 4))

for i in range(1, 6):
    print(" " * (5 - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    print("")

for i in range(1, 6):
    print(" " * (5 - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print("")

for i in range(1, 6):
    print(" " * (5 - i), end="")
    for j in range(i, 0, -1):
        print(j, end="")
    for j in range(1 + 1, i + 1):
        print(j, end="")
    print("")

for i in range(1, 6):
    if i == 1:
        print(i)
    elif i < 5:
        print("1", end="")
        print(" " * (i - 1), end="")
        print(i)
    else:
        for j in range(1, 6):
            print(j, end="")
        print("")

for i in range(1, 6):
    print(" " * (5 - i), end="")
    for j in range(1, i + 1):
        print(j + i - 1, end="")
    print("")

for i in range(1, 6):
    print(" " * (5 - i), end="")
    for j in range(1, i + 1):
        print(j + i - 1, end="")
    for j in range(j + i - 1, i, -1):
        print(j-1, end="")
    print("")

