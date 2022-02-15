Bingo = list()
Calling = []

for _ in range(5):
    Bingo.append(list(map(int,input().split())))
for _ in range(5):
    Calling += (list(map(int,input().split())))

line = [0]*12

cnt = 0
for number in Calling:
    for i in range(5):
        if Bingo[i].count(number):
            line[i] += 1
            line[5+Bingo[i].index(number)] += 1

            if i == Bingo[i].index(number):
                line[10] += 1
            if i == 4-Bingo[i].index(number):
                line[11] += 1
    cnt += 1

    if (line.count(5)>=3):
        break

print(cnt)