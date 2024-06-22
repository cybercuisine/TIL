from collections import defaultdict


H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]

def check(a, b, d):
    if a + d >= H or a - d < 0 or b + d >= W or b - d < 0:
        return False

    if C[a][b] != '#':
        return False

    if (C[a + d][b + d] == '#' and C[a + d][b - d] == '#' and
            C[a - d][b + d] == '#' and C[a - d][b - d] == '#'):
        return True

    return False


S = defaultdict(int)

for i in range(1, H):
    for j in range(1, W):
        if C[i][j] == '.':
            continue
        size = 0
        while True:
            if check(i, j, size + 1):
                size += 1
            else:
                break
        S[size] += 1

for i in range(1, min(H, W) + 1):
    print(S[i], end=' ')
print()