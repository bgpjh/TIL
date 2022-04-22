N, X = map(int, input().split())

Data = list(map(int, input().split()))

for d in Data:
    if d < X:
        print(d, end=' ')
print()