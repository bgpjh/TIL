T = int(input())
FIBO = [[0,0]]*41
FIBO[0] = [1,0]
FIBO[1] = [0,1]

for i in range(2,41):
    FIBO[i] = [FIBO[i-2][0] + FIBO[i-1][0], FIBO[i-2][1] + FIBO[i-1][1]]

for _ in range(T):
    N = int(input())
    print('{} {}'.format(FIBO[N][0],FIBO[N][1]))