S = input()
P = "atcoder"
N = len(P)
L = [P.index(c) for c in S]

ans = 0
for i in range(N - 1):
    for j in range(N - i - 1):
        if L[j] > L[j + 1]:
            L[j], L[j + 1] = L[j + 1], L[j]
            ans += 1
print(ans)
