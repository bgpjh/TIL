H, M = map(int, input().split())

m = M - 45

if m < 0:
    h = (H-1)%24
    m += 60
else:
    h = H

print('{} {}'.format(h,m))