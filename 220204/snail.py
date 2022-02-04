T = int(input())

for tc in range(1,T+1):
    N = int(input())
    S = list()

    for i in range(N):
        S.append([0 for x in range(N)])

    X,Y = 0,0
    dir = 0 # 0:right , 1:down, 2:left, 3:up

    for i in range(1,N**2+1):
        S[Y][X] = i
        if (dir==0): #go right
            if (X+1>=N) or (S[Y][X+1]!=0):
                dir = 1
                Y += 1
            else:
                X += 1
        elif (dir==1): #go down
            if (Y+1>=N) or (S[Y+1][X]!=0):
                dir = 2
                X -= 1
            else:
                Y += 1
        elif (dir==2): #go left
            if (X-1<0) or (S[Y][X-1]!=0):
                dir = 3
                Y -= 1
            else:
                X -= 1
        elif (dir==3):
            if (Y-1<0) or (S[Y-1][X]!=0):
                dir = 0
                X += 1
            else:
                Y -= 1

    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(S[i][j],end = " ")
        print("")