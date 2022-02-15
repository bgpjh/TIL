N = int(input())
Line = list()
V = list(map(int,input().split()))

for i in range(1,N+1):
    Line.insert(i-V[i-1]-1,i)

for i in range(N):
    print(Line[i],end=' ')
print()