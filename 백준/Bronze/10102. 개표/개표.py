score_board = [0, 0]

V = int(input())
score = input()

for one in score:
    if one == 'A':
        score_board[0] += 1
    else:
        score_board[1] += 1

if score_board[0] == score_board[1]:
    print('Tie')
elif score_board[0] > score_board[1]:
    print('A')
else:
    print('B')