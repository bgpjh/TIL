T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    P = list(map(int, input().split()))

    D = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    for p in P:
        for n in range(1,p):
            D[n] += 1

    L = [0] * N

    i = 0
    K = 1
    while L[M] == 0:
        if L[i] == 0:
            if (D[P[i]] == 0):
                L[i] = K
                for n in range(1,P[i]):
                    D[n] -= 1
                K += 1
        
        i += 1
        if i >= N:
            i = 0

    print(L[M])