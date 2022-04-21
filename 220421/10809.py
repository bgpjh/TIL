S = list(map(str,input()))
A = [-1]*26

index = 0
for s in S:
    I = (ord(s) - ord('a'))
    if A[I] == -1:
        A[I] = index
    index += 1

for a in A:
    print(a, end=' ')
print()