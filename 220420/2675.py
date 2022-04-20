tc = int(input())

for _ in range(tc):
    N,T = map(str,input().split())
    T = ' '.join(T).split()
    print(N)

    for t in T:
        print(t * int(N), end='')
    print()