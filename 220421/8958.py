N = int(input())

for _ in range(N):
    Data = list(map(str,input()))

    score = 0
    index = 0

    for d in Data:
        if d == 'O':
            index += 1
            score += index
        else:
            index = 0

    print(score)