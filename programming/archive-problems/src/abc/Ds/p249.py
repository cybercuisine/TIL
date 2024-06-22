from collections import Counter

N = int(input())
A = list(map(int, input().split()))

C = Counter(A)
ans = 0
A_max = 2 * 10 ** 5

for i in range(1, A_max + 1):
    for j in range(i, A_max + 1, i):
        k = j // i
        ans += C[i] * C[j] * C[k]
print(ans)