N = int(input())
A = list(map(int, input().split()))
Q = int(input())

lrs = [list(map(int, input().split())) for i in range(Q)]

wins = []
lose = []
for i in range(N):
    if i == 0:
        wins.append(A[i])
        lose.append(abs(A[i]-1))
    else:
        wins.append(wins[i-1]+A[i])
        lose.append(lose[i-1]+abs(A[i]-1))
        
for lr in lrs:
    lottery = 0
    L = lr[0] - 1
    R = lr[1] - 1
    if L == 0:
        lottery = wins[R] - lose[R]
    else:
        lottery = wins[R] - wins[L-1] - lose[R] + lose[L-1]
    
    if lottery == 0:
        print("draw")
    elif lottery > 0:
        print("win")
    else:
        print("lose")