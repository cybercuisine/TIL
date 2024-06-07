def move(board):
    board = [list(x) for x in zip(*board)]
    for i in range(len(board)):
        row = board[i]
        row = [i for i in row if i!=0]
        n = len(board[i]) - len(row)
        row.extend([0]*n)
        board[i] = row
    board = [list(x) for x in zip(*board)]
    return board

ls_ans = []
while(1):
    ans = 0
    H = int(input())
    if H==0:
        break
    board = []
    for h in range(H):
        C = list(map(int,input().split()))
        board.append(C)
    board = board[::-1]
    for t in range(H):
        for h in range(H):
            C = board[h]
            changed = set()
            old_c = ''
            oldold_c = ''
            streak = 0
            for i,c in enumerate(C):
                if c == old_c and c == oldold_c:
                    if streak == 0:
                        streak += 3*c
                        C[i] = C[i-1] = C[i-2] = 0
                    else:
                        streak += c
                        C[i] = 0
                else:
                    ans += streak
                    streak = 0
                oldold_c = old_c
                old_c = c
            ans += streak
            board[h] = C
        board = move(board)
    ls_ans.append(ans)

for ans in ls_ans:
    print (ans)