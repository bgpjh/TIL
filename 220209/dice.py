dice_set = [5,3,4,1,2,0]

def maxV(vlist):
    value = 0
    for v in vlist:
        if v >= value:
            value = v
    return value

def sumV(vlist,N):
    total = 0
    for i in range(N):
        total += maxV(vlist[i])
    return total

def diceTop(vlist,N,i):
    number = i
    val = list()
    for i in range(N):
        top = vlist[i].index(number)
        bottom = dice_set[top]

        temp = list()
        for j in range(6):
            if (j != top) and (j != bottom):
                temp.append(vlist[i][j])

        val.append(temp)
        number = vlist[i][bottom]
    return val

N = int(input())

dice = list()

for _ in range(N):
    dice.append(list(map(int, input().split())))

sum_list = list()
for i in range(1,7):
    dice_top = diceTop(dice,N,i)
    sum_list.append(sumV(dice_top,N))

print(maxV(sum_list))