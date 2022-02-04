T = int(input())

for tc in range(1,T+1):

    sudoku = []
    for i in range(9):
        a = list(map(int,input().split()))
        sudoku.append(a)
    checker = 1
    
    for vertical in range(9):
        check = set(sudoku[vertical])
        if len(check) != 9:
            checker = 0

    vsudoku = list(map(list,zip(*sudoku)))
    for horizon in range(9):
        check = set(vsudoku[horizon])
        if len(check) != 9:
            checker = 0

    square = [[],[],[],[],[],[],[],[],[]]
    temp = list()
    for i in range(9):
        for j in range(9):
            temp.append(sudoku[i][j])

    for i in range(len(temp)):
        square[(i//27*3)+((i%9)//3)].append(temp[i])

    for box in range(9):
        check = set(square[box])

        if len(check) != 9:
            checker = 0

    print("#{} {}".format(tc, checker))