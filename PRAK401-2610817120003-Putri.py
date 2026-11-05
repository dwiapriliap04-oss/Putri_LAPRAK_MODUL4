input_data = input().split()
kelipatan = int(input_data[0])
simbol = input_data[1]

output_list = []
for i in range(1, 51):
    if i % kelipatan == 0:
        output_list.append(simbol)
    else:
        output_list.append(str(i))

print(" ".join(output_list))