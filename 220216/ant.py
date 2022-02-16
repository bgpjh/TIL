MAP = list(map(int, input().split())) # W,H
POS = list(map(int, input().split())) # X,Y

t = [0, 0]
t[0] = t[1] = int(input())
t[0] %= (2*MAP[0])
t[1] %= (2*MAP[1])

d = [1, -1]
for i in range(2):
    index = 0
    for _ in range(t[i]):
        POS[i] += d[index]
        if POS[i] == MAP[i]:
            index = 1
        if POS[i] == 0:
            index = 0

print(POS[0], POS[1])