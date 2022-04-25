N = int(input())
INDEX = [0]*51
count = [0]*51
DATA = list()
for _ in range(N):
    data = input()
    L = len(data)
    count[L] += 1

    for i in range(L,51):
        INDEX[i] += 1
    

    if count[L] > 1:
        for i in range(INDEX[L-1],INDEX[L]):
            if data <= DATA[i]:
                DATA.insert(i,data)
                break
    else:
        DATA.insert(INDEX[L-1],data)

    print(INDEX)
    print(DATA)

prev = ''
for d in DATA:
    if d != prev:
        prev=d
        print(d)