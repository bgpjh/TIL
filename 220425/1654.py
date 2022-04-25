K,N = map(int,input().split())
DATA = list()
for _ in range(K):
    temp = int(input())
    DATA.append(temp)

l = 1
r = max(DATA)
m = (l+r) // 2

while l <= r:
    m = (l+r) // 2

    c = 0
    for d in DATA:
        c += d // m
    
    if c >= N:
        l = m + 1
    else:
        r = m - 1

print(r)