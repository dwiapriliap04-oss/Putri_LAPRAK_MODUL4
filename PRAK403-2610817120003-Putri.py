input_data = input().split()
a = int(input_data[0])
b = int(input_data[1])

if a < b:
    for i, j in zip(range(a, b + 1), range(b, a - 1, -1)):
        print(f"{i} {j}", end="")
        if i < b:
            print(" - ", end="")
else:
    for i, j in zip(range(a, b - 1, -1), range(b, a + 1)):
        print(f"{i} {j}", end="")
        if i > b:
            print(" - ", end="")
print()