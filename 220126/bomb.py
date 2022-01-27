T = int(input())

def drop(x,H,W,Map):
    for h in H:
        if Map[h][x] != 0:
            bomb(h,x,H,W,Map)

def bomb(y,x,H,W,Map):
    power = Map[y][x]
    Map[y][x] = 0
    if power <= 1:
        pass
    else:
        for p in range(1,power):
            if y-p >= 0:
                bomb(y-p,x,H,W,Map)
            if y+p <= H:
                bomb(y+p,x,H,W,Map)
            if x-p >= 0:
                bomb(y,x-p,H,W,Map)
            if x+p >= W:
                bomb(y,x+p,H,W,Map)

def sortblock(H,W,Map):
    for w in range(W):
        index = H
        for h in range(H,-1,-1):
            if Map[h][w] == 0:
                index = H
            else:
                Map[index][w] = Map[h][w]
                Map[h][w] = 0
                index = h

for test_case in range(1,T+1):
    temp = list(map(int, (input().split())))
    N,W,H = temp[0],temp[1],temp[2]
    Map = []
    for h in range(H):
         Map.append(list(map(int, input().split())))
    min_test = W*H