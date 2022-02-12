dwarf = list()

for _ in range(9):
    dwarf.append(int(input()))

for index in range(9):
    for N in range(index,9):
        if dwarf[index] > dwarf[N]:
            dwarf[index], dwarf[N] = dwarf[N], dwarf[index]

total = 0
for i in range(9):
    total += dwarf[i]

fake = list()

for i in range(8,0,-1):
    test = total
    test -= dwarf[i]
    for j in range(i-1,-1,-1):
        if test - dwarf[j] == 100:
            fake = [i,j]
            break

result = list()
for index in range(9):
    if index not in fake:
        print(dwarf[index])