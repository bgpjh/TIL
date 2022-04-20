N = int(input())
data = list(map(int, input().split()))
M = 0
S = 0
for d in data:
    S += d
    if d > M:
        M = d

print('{}'.format(S*100/M/N))