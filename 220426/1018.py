B1 = [['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W']]

B2 = [['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],]

def Board(I,J,C):
    mini = C
    board = list()
    for k in range(8):
        temp = MAP[J+k][I:I+8]
        board.append(temp)
    #print(board)

    cnt1 = 0
    cnt2 = 0

    for i in range(8):
        for j in range(8):
            if board[i][j] != B1[i][j]:
                cnt1 += 1
            if board[i][j] != B2[i][j]:
                cnt2 += 1

    if cnt1 < mini:
        mini = cnt1
    if cnt2 < mini:
        mini = cnt2
    return mini


M,N = map(int, input().split())

MAP = list()
for _ in range(M):
    MAP.append(list(map(str,input())))

CN = 64

for i in range(N-7):
    for j in range(M-7):
        CN = Board(i,j,CN)

print(CN)