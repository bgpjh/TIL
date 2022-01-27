#박지하
T = int(input())

for tc in range(1,T+1):
    N,M = list(map(int,input().split()))

    a = list(map(int,input().split())) # 리스트

    sum_list =[] # 구간합을 모아두는 리스트
    for i in range(N-M+1):
        value = 0
        for j in range(M):
            value += a[i+j]
        sum_list += [value]
        value = 0

    print('#{} {}'.format(tc,max(sum_list)-min(sum_list)))