A = int(input())
B = int(input())
C = int(input())

DATA = list(map(str,str(A*B*C)))
Num = [0,0,0,0,0,0,0,0,0,0]

for d in DATA:
    Num[int(d)] += 1

for n in Num:
    print(n)