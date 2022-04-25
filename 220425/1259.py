while True:
    S = input()
    Sr = S[::-1]

    if S=='0':
        break
    elif S==Sr:
        print('yes')
    else:
        print('no')