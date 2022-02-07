T = int(input())

def killing(X,Y,M,MAP):
    kill_sum = 0
    for i in range(M):
        for j in range(M):
            kill_sum += MAP[X+i][Y+j]
    return kill_sum

for tc in range(1,T+1):
    N, M = map(int,input().split())

    fly = list()
    for n in range(N):
        fly.append(list(map(int,input().split())))

    kill = list()
    for I in range(N-M+1):
        for J in range(N-M+1):
            kill.append(killing(I,J,M,fly))
    
    print('#{} {}'.format(tc,max(kill)))