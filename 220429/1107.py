N = int(input())
m = int(input())
data = [1] * 1000000
NUM = list()

if m>0:
    NUM = list(map(int, input().split()))

i = 0
ca = True
if N > 100:
    mini = N-100
else:
    mini = 100-N

while i<1000000:
    ca = True
    ch = list(map(int,str(i)))
    for c in ch:
        if c in NUM:
            data[i] = 0
            ca = False
            break

    if ca:
        if abs(i-N)+len(ch) < mini:
            mini = abs(i-N)+len(ch)
    i += 1

print(mini)

# if 0 < m < 10:
#     T = N
#     B = N
#     while True:
#         sT = 