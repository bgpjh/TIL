M = 0
I = 0
for i in range(1,10):
    V = int(input())
    if V > M:
        M = V
        I = i

print(M)
print(I)