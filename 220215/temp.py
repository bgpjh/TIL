N,K = map(int,input().split())

Temp = list(map(int,input().split()))
temp_sum = [0]
ts = 0
for i in range(N):
    ts += Temp[i]
    temp_sum.append(ts)

max_num = temp_sum[K] - temp_sum[0]
for i in range(N-K+1):
    val = temp_sum[i+K] - temp_sum[i]
    if max_num < val:
        max_num = val


print(max_num)