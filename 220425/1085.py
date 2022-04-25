x,y,w,h = map(int, input().split())

A = x
B = y
C = w-x
D = h-y
print(min(A,B,C,D))