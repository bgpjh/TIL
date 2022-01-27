
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    #a = list(map(int, input().split()))
    a = map(int, input().split())
    minV,maxV = 1000001,0
    for value in a:
        if minV > value:
            minV = value
        if maxV < value:
            maxV = value
    print('#{} {}'.format(tc,maxV-minV))