L = [0] * 42
cnt = 0

for _ in range(10):
    N = int(input())
    if L[N%42] == 0:
        L[N%42] += 1
        cnt += 1

print(cnt)