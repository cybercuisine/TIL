from itertools import permutations

K = int(input())
N = 8
queens = [list(map(int, input().split())) for _ in range(K)]



def judge(ls):
    board = []
    for i in range(N):
        board.append([i, ls[i]])
    for queen in queens:
        if queen not in board:
            return False
    
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            [x1, y1] = board[i]
            [x2, y2] = board[j]
            if abs(x1 - x2) == abs(y1 - y2):
                return False

    return True

def build(ls):
    arr = []
    for i in range(N):
        string = ''
        for j in range(N):
            if ls[i] == j:
                string += 'Q'
            else:
                string += '.'
        arr.append(string)
    return arr

for ls in permutations(range(N)):
    if judge(ls):
        arr = build(ls)
        for a in arr:
            print(a)
        exit()