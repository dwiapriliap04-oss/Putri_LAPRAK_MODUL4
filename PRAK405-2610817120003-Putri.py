input_data = input().split()
n = int(input_data[0])
kelipatan = int(input_data[1])

total_keseluruhan = 0

for i in range(1, n + 1):
    baris_str = []
    total_baris = 0
    for j in range(i, 0, -1):
        baris_str.append(f"({j} * {kelipatan})")
        total_baris += j * kelipatan
    
    total_keseluruhan += total_baris
    teks_baris = " + ".join(baris_str)
    print(f"{teks_baris} = {total_baris}")

print(total_keseluruhan)