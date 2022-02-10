N = int(input())
store = list()

top = [[0,0]]
cnt = 0
for _ in range(N):
    LH = list(map(int,input().split()))
    store.append(LH)
    if LH[1] > top[0][1]:
        top = [LH]
        cnt = 0
    elif LH[1] == top[0][1]:
        top.append(LH)
        cnt += 1


for i in range(N):
    for j in range(N-i-1):
        if store[j] > store[j+1]:
            store[j], store[j+1] = store[j+1], store[j]

area = (top[cnt][0]-top[0][0]+1) * top[0][1]
indexLeft = store.index(top[0])
indexRight = store.index(top[cnt])

height = store[0][1]
pos = 0
for i in range(store[0][0],store[indexLeft][0]):
    if i == store[pos+1][0]:
        pos += 1
        if height < store[pos][1]:
            height = store[pos][1]
    area += height

height = store[N-1][1]
pos = N-1
for i in range(store[N-1][0],store[indexRight][0],-1):
    if i == store[pos-1][0]:
        pos -= 1
        if height < store[pos][1]:
            height = store[pos][1]
    area += height

print(area)