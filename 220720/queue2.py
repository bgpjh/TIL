import heapq

T = int(input())

for tc in range(1,T+1):
    minQ = []
    maxQ = []
    checker = dict()
    count = 0

    K = int(input())

    for k in range(K):
        O, V = input().split()

        if O == 'I':
            V = int(V)
            heapq.heappush(minQ,V)
            heapq.heappush(maxQ,-V)
            if checker.get(V):
                checker[V] += 1
            else:
                checker[V] = 1
            count += 1

        elif O == 'D' and count > 0:
                if V == '1':
                    max_value = heapq.heappop(maxQ)
                    # print(max_value, 'maxQ : ', maxQ)
                    while not checker[-max_value]:
                        max_value = heapq.heappop(maxQ)
                        # print(max_value, 'maxQ : ', maxQ)
                    checker[-max_value] -= 1
                    count -= 1
                elif V == '-1':
                    min_value = heapq.heappop(minQ)
                    # print(min_value, 'minQ : ', minQ)
                    while not checker[min_value]:
                        min_value = heapq.heappop(minQ)
                        # print(min_value, 'minQ : ', minQ)
                    checker[min_value] -= 1
                    count -= 1
    
        # print('max : ',maxQ, 'min : ',minQ, 'checker : ',checker, 'count : ',count)

    if count > 0:
        max_value, min_value = 0,0
        while True:
            max_value = -heapq.heappop(maxQ)
            if checker[max_value]:
                break
        while True:
            min_value = -heapq.heappop(minQ)
            if checker[min_value]:
                break

        print(max_value,min_value)
    else:
        print('EMPTY')