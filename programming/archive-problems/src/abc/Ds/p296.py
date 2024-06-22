N, M = map(int, input().split())
ans = float('inf')

for a in range(1, N + 1):
    b = -(-M // a)
    if b > N:
        continue
    if b < a:
        break
    ans = min(ans, a * b)

print(ans if ans != float('inf') else -1)