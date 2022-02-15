for tc in range(1,5):
    ax1,ay1,ax2,ay2,bx1,by1,bx2,by2 = map(int,input().split())
    if ax1>bx1:
        ax1,ay1,ax2,ay2,bx1,by1,bx2,by2 = bx1,by1,bx2,by2,ax1,ay1,ax2,ay2

    ans = 'Fail'
    if (bx1 > ax2) or (by1 > ay2):
        ans = 'd'
    elif (ax1 < bx1 <= ax2) and ((by1 == ay2) or (by2 == ay1)):
        if (bx1 == ax2):
            ans = 'c'
        ans = 'b'

    if (ax1 <= bx1 < ax2 and ay1<= by1 < ay2) or (ax1 < bx2 <= ax2 and ay1 < by2 <= ay2):
        ans = 'a'
    elif (bx1 == ax2 and ay1 <= by1 < ay2) or (ax1 <= bx1 < ax2 and by1 == ay2) or (ax1<= bx2< ax2 and by2 == ay1):
        ans = 'b'