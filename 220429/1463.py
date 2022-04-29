N = int(input())
INDEX = [N]*(N+1)

INDEX[N] = 0

for i in range(N,0,-1):
    if i%3==0:
        if INDEX[i//3] > INDEX[i]+1:
            INDEX[i//3] = INDEX[i]+1
    if i%2==0:
        if INDEX[i//2] > INDEX[i]+1:
            INDEX[i//2] = INDEX[i]+1
    if i>0:
        if INDEX[i-1] > INDEX[i]+1:
            INDEX[i-1] = INDEX[i]+1

print(INDEX[1])