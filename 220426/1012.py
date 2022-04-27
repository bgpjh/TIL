T = int(input())

dx = [-1,0,1,0]
dy = [0,-1,0,1]


def close(X,Y,M,N):
    MAP[Y][X] = 2
    global remain
    remain -= 1

    for i in range(4):
        x = X + dx[i]
        y = Y + dy[i]
        if 0<=x<M and 0<=y<N and MAP[y][x]==1:
            close(x,y,M,N)


def find(M,N,K):
    X = 0
    Y = 0
    cnt = 0
    global remain
    while remain > 0:
        if MAP[Y][X] == 1:
            cnt += 1
            close(X,Y,M,N)
        X += 1
        if X>=M:
            X = 0
            Y += 1

    return cnt


for tc in range(T):
    M,N,K = map(int,input().split())

    MAP = list()
    for _ in range(N):
        MAP.append([0]*M)

    for _ in range(K):
        X, Y = map(int, input().split())
        MAP[Y][X] = -1

    remain = K
    ans = find(M,N,K)

    print(ans)