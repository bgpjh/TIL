paper = [[0 for _ in range(100)] for _ in range(100)]

N = int(input())
cnt = 0
for _ in range(N):
    X,Y = map(int,input().split())

    for i in range(10):
        for j in range(10):
            if paper[X+j][Y+i] == 0:
                cnt += 1
                paper[X+j][Y+i] = 1

print(cnt)