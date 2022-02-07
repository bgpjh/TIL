for tc in range(1,11):
    t = int(input())

    ladder = list()
    for i in range(100):
        ladder.append(list(map(int,input().split())))

    depth = 99
    x = ladder[99].index(2)

    while depth > 0:
        ladder[depth][x] = 2
        if (x>0 and ladder[depth][x-1]==1):
            x -= 1
        elif (x<99 and ladder[depth][x+1]==1):
            x += 1
        else:
            depth -=1
    print("#{} {}".format(t, x))