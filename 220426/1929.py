from math import sqrt


M,N = map(int, input().split())
ans = [1]*(N+1)
ans[0] = 0
ans[1] = 0

for i in range(2,int(sqrt(N)+1)):
    if ans[i] == 1:
        for k in range(i+i,N+1,i):
            ans[k] = 0

for i in range(M,N+1):
    if ans[i] == 1:
        print(i)