T = int(input())

for tc in range(1,T+1):
    N,K = map(int,input().split())

    MAP_H = list()
    for i in range(N):
        MAP_H.append(list(map(int,input().split())))

    temp = list(zip(*MAP_H))
    MAP_V = list()
    for i in range(N):
        MAP_V.append(list(temp[i]))

    cnt = 0
    for line in MAP_H:
        index = 0
        while (index != len(line)-1):
            if (line[index]!=0 and line[index+1]!=0):
                line[index]+=line.pop(index+1)
            else:
                index += 1
        cnt += line.count(K)
    
    for line in MAP_V:
        index = 0
        while (index != len(line)-1):
            if (line[index]!=0 and line[index+1]!=0):
                line[index]+=line.pop(index+1)
            else:
                index += 1
        cnt += line.count(K)

    print('#{} {}'.format(tc,cnt))