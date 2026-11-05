batas = int(input())

ganjil = []
for i in range(1, batas + 1):
    if i % 2 != 0:
        ganjil.append(i)
print(ganjil)

genap = []
for i in range(batas, 1, -1):
    if i % 2 == 0:
        genap.append(i)
print(genap)