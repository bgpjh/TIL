N = int(input())

L = list(map(int,input().split()))

maxLength = 1
minLength = 1

maxCount = 1
minCount = 1
for i in range(1,N):
    if L[i] > L[i-1]:
        maxCount += 1
        if minLength < minCount:
            minLength = minCount
        minCount = 1
    elif L[i] < L[i-1]:
        minCount += 1
        if maxLength < maxCount:
            maxLength = maxCount
        maxCount = 1
    else:
        maxCount += 1
        minCount += 1

if minLength < minCount:
    minLength = minCount
if maxLength < maxCount:
    maxLength = maxCount

print(maxLength) if maxLength>=minLength else print(minLength)