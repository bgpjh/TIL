for tc in range(1,11):
    width = int(input()) # 가로 길이

    build = list(map(int,input().split())) # 건물의 높이를 리스트로 입력받음

    icansee = 0 # 반환값

    for i in range(width):
        if build[i]==0: # 건물이 없을경우 무시 (0)
            continue
        else: # 건물의 왼쪽 2칸, 오른쪽 2칸 비교
            builds = [build[i-2],build[i-1],build[i+1],build[i+2]] # 비교할 대상 리스트
            # if build[i] - max(builds) > 0:
            #     icansee += build[i] - max(builds)

            maxHeight = 0
            for height in builds:
                if maxHeight < height:
                    maxHeight = height
            
            if build[i] - maxHeight > 0:
                icansee += build[i] - maxHeight

    print('#{} {}'.format(tc,icansee))