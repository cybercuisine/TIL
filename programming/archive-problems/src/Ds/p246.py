def f(a, b):
    return a * a * a + a * a * b + a * b * b + b * b * b

N = int(input())
MAX = 10 ** 6
ans = float('inf')

for a in range(MAX + 1):
    left = 0
    right = MAX
    while left <= right:
        mid = (left + right) // 2
        X = f(a, mid)
        if X < N:
            left = mid + 1
        else:
            right = mid - 1
    if left <= MAX:
        X = f(a, left)
        if X >= N:
            ans = min(ans, X)
    if left > 0:
        X = f(a, left - 1)
        if X >= N:
            ans = min(ans, X)

print(ans)
