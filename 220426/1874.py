n = int(input())
target = list()
for _ in range(n):
    target.append(int(input()))

store = list()
answer = list()
index = 0
pr = list()

for f in range(1,n+1):
    store.append(f)
    pr.append('+')
    while len(store) > 0 and store[-1] == target[index]:
        answer.append(store.pop())
        index += 1
        pr.append('-')

if len(store) == 0:
    for p in pr:
        print(p)
else:
    print('NO')