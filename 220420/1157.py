Data = list(map(str,input().upper()))
SET = dict()
for d in Data:
    if d in SET:
        SET[d] += 1
    else:
        SET[d] = 1

maximum = 0
alpha = ''
duple = False
for d in SET.keys():
    if SET[d] > maximum:
        maximum = SET[d]
        duple = False
        alpha = d
    elif SET[d] == maximum:
        duple = True

print('?') if duple else print('{}'.format(alpha))