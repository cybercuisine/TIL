def solve():
    H, W, K = map(int, input().split())
    board = []
    for i in range(H):
        S = input()
        A = []
        for s in S:
          A.append(int(s))
        board.append(A)
        
    def calculate_score(board):
        total_score = 0
        combo = 0
        while True:
            to_clear = set()
            for i in range(H):
                for j in range(W - K + 1):
                  
                    if len(set(board[i][j:j + K])) == 1 and board[i][j] != 0:
                        for k in range(K):
                            to_clear.add((i, j + k))
            
            if not to_clear:
                break
            score = 0
            for i, j in to_clear:
                score += board[i][j]
                board[i][j] = 0
            total_score += (2 ** combo) * score
            combo += 1

            for j in range(W):
                stack = []
                for i in range(H):
                    if board[i][j] != 0:
                        stack.append(board[i][j])
                for i in range(H):
                    if stack:
                        board[H - 1 - i][j] = stack.pop()
                    else:
                        board[H - 1 - i][j] = 0
                        
        return total_score
        
    def drop_stones(board):
        for j in range(W):
            stack = []
            for i in range(H):
                if board[i][j] != 0:
                    stack.append(board[i][j])
            for i in range(H):
                if stack:
                    board[H - 1 - i][j] = stack.pop()
                else:
                    board[H - 1 - i][j] = 0
        return board
    
    max_score = 0
    for i in range(H):
        for j in range(W):
            temp_board = [row[:] for row in board]
            temp_board[i][j] = 0
            temp_board = drop_stones(temp_board)
            score = calculate_score(temp_board)
            if score > max_score:
                max_score = score
                
    print(max_score)

solve()