#박지하
T = int(input())

for tc in range(1, T+1):
    K,N,M = list(map(int,input().split()))
    ECS = list(map(int,input().split()))
    ECS += [N]

    elec = K
    chargeNum = 0
    passedECS = 0

    for p in range(1,N+1):
        if p==N: # 목적지 도달시 break
            break
        elec -= 1
        if p in ECS: # 다음 정류장까지 전기 부족시 충전
            if elec < ECS[passedECS+1]-ECS[passedECS]:
                chargeNum += 1
                elec = K
            passedECS += 1
        if elec == 0: # 주행중 연료 0일경우 0 반환 break
            chargeNum = 0
            break
    print('#{} {}'.format(tc, chargeNum))