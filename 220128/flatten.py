for tc in range(1,11):
    maxdump = int(input())
    width = list(map(int,input().split()))
    for dump in range(maxdump):
        width[width.index(max(width))] -= 1
        width[width.index(min(width))] += 1

    print('#{} {}'.format(tc, max(width)-min(width)))