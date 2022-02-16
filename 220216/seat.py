W, H = map(int, input().split())
K = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

if K>W*H:
    print(0)
else:
    i = 0
    outer = 2*(W+H) - 4
    while outer < K:
        K -= outer
        outer -= 8
        i += 1

    W -= 2*i
    H -= 2*i

    X = 1
    Y = 1
    index = 0
    for R in range(1, K):
        if R == H:
            index += 1
        if R == H+W-1:
            index += 1
        if R == H+W+H-2:
            index += 1
        X += dx[index]
        Y += dy[index]

    print(X+i, Y+i)