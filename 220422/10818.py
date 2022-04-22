N = int(input())

Data = list(map(int,input().split()))

max_num = Data[0]
min_num = Data[0]
for i in range(N):
    if max_num < Data[i]:
        max_num = Data[i]
    if min_num > Data[i]:
        min_num = Data[i]

print('{} {}'.format(min_num, max_num))