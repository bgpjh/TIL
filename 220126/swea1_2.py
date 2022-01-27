T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    c = input()
    card_list = []
    card_list.extend(c)
    ans = dict()
    for card in card_list:
        if card not in ans:
            ans[card] = 0
        ans[card] += 1
    max_card = 0
    card_num = 0
    for card in ans.items():
        if card[1] > max_card:
            max_card = card[1]
            card_num = int(card[0])
        elif card[1] == max_card and int(card[0]) > card_num:
            max_card = card[1]
            card_num = int(card[0])
    print('#{} {} {}'.format(test_case, card_num, max_card))