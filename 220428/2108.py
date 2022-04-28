N = int(input())
s = 0
mini = 4001
maxi = -4001
li = list()
for _ in range(N):
    D = int(input())
    li.append(D)
    s += D
    if mini > s:
        mini = s
    if maxi < s:
        maxi = s

print(int((s/N)+0.5))
print((li.sort())[N//2)])
print(N)
print(maxi-mini)