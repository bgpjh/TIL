def ABS(value):
    if value >= 0:
        return value
    else:
        return -value

LENGTH = list(map(int,input().split())) # W,H 0 = 가로 1 = 세로

count = int(input())
shop = list()
for i in range(count):
    shop.append(list(map(int,input().split())))

POS = list(map(int,input().split()))

dis = 0
for value in shop:
    if POS[0] == value[0]: # 1 북 2 남 3 서 4 동 # 같은 줄이면
        dis += ABS(POS[1]-value[1])
    else: # POS[0]//2 > 0 = 위아래 / 1 = 왼쪽오른쪽 # 다른 줄이면
        if POS[0]//3 == value[0]//3: # 반대 방향일 때 , 1 : POS=서,동 // 0 : POS=북,남
            d = POS[1] + value[1]
            dis += LENGTH[not POS[0]//3]
            if d >= LENGTH[POS[0]//3]:
                dis += 2*LENGTH[POS[0]//3] - d
            else:
                dis += d
        else: # 인접 방향일 때
            if POS[0]%2: # 참 => POS = 남,동 / 거짓 => POS = 북,서
                dis += value[1]
            else:
                dis += LENGTH[not POS[0]//3] - value[1]
            
            if value[0]%2:
                dis += POS[1]
            else:
                dis += LENGTH[not value[0]//3] - POS[1]

print(dis)