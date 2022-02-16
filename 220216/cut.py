W, H = map(int, input().split())

N = int(input())
cut = [list(),list()]
count = [0,0]
width = list()
height = list()

for i in range(N):
    D, C = map(int,input().split())
    cut[D].append(C-1)
    count[D] += 1

length = 0
for index in range(W):
    length += 1
    if index in cut[1]:
        width.append(length)
        length = 0
width.append(length)

length = 0
for index in range(H):
    length += 1
    if index in cut[0]:
        height.append(length)
        length = 0
height.append(length)

min = [0,0]

for v in width:
    if min[0] < v:
        min[0] = v

for v in height:
    if min[1] < v:
        min[1] = v

print(min[0]*min[1])