answers = []

while True:
    N, X = map(int, input().split())
    if N == 0 and X == 0:
        break
    ans = 0
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            k = X - (i + j)
            if k > j and k <= N:
                ans += 1
    answers.append(ans)

print(*answers,sep='\n')