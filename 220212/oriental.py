K = int(input())

length = [[],[],[],[]]
I = list()

for _ in range(6):
    N,L = list(map(int,input().split()))
    I.append(N-1)
    length[N-1].append(L)

longWidth = list()
for i in range(4):
    if I.count(i) == 1:
        longWidth.append(i)

Area = length[longWidth[0]][0] * length[longWidth[1]][0]
length[longWidth[0]].append(0)
length[longWidth[1]].append(0)

while (I[0] not in longWidth) or (I[1] not in longWidth):
    Num = I[0]
    I.append(I.pop(0))
    length[Num][0], length[Num][1] = length[Num][1], length[Num][0]

Area -= length[I[3]][0] * length[I[4]][1]
Area *= K

print(Area)