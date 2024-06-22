N = int(input())
S = input()

if S.count('-') == 0 or S.count('-') == N:
    print(-1)
    exit()

X = -1
i = 0
while i < N:
    if S[i] != 'o':
        i += 1
        continue
    size = 1
    for j in range(i + 1, N):
        if S[j] == '-':
            break
        else:
            size += 1
    X = max(X, size)
    i += (size + 1)

print(X)