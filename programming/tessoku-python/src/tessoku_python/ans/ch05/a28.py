N = int(input())

X = 0
T = [None] * N
A = [None] * N
for i in range(N):
    T[i], A[i]= map(str, input().split())

for i in range(N):
    if T[i] == "+":
        X += int(A[i])
    elif T[i] == "-":
        X -= int(A[i])
    else:
        X *= int(A[i])
    
    if X < 0:
        X += 10000
    X %= 10000

    print(X)