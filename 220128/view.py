for tc in range(1,11):
    width = int(input())

    build = list(map(int,input().split()))

    icansee = 0

    for i in range(width):
        if build[i]==0:
            continue
        else:
            builds = [build[i-2],build[i-1],build[i+1],build[i+2]]
            if build[i] - max(builds) > 0:
                icansee += build[i] - max(builds)

    print('#{} {}'.format(tc,icansee))