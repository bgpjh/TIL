def find(key):
    l = 0
    r = len(Data)-1
    m = (l + r)//2

    while r >= l:
        if Data[m] == key:
            return 1
        
        if Data[m] > key:
            r = m-1
            m = (l+r)//2
        else:
            l = m+1
            m = (l+r)//2

    return 0


N = int(input())

Data = list(map(int, input().split()))
Data.sort()

M = int(input())
Key = list(map(int, input().split()))

for k in Key:
    print(find(k))