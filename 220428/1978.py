Number = [1]*1001
Number[0] = 0
Number[1] = 0
for i in range(2,1001):
    if Number[i] == 1:
        for j in range(2*i,1001,i):
            Number[j] = 0

N = int(input())
data = list(map(int, input().split()))
sum = 0
for d in data:
    sum += Number[d]
print(sum)