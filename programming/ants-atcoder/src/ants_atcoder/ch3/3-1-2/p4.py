def f(x):
    return a * x**3 + b * x**2 + c * x + d


def check(high, target):
    if f(high) * f(target) < 0:
        return False
    return True


def add_solution(x):
    if x > eps:
        ans[t][0] += 1
    elif x < -eps:
        ans[t][1] += 1



T = int(input())
ans = [[0, 0] for _ in range(T)]
eps = 10 ** (-6)
for t in range(T):
    a, b, c, d = map(int, input().split())
    if b**2 - 3 * a * c >= 0:
        x1 = (-b - (b**2 - 3 * a * c) ** 0.5) / (3 * a)
        x2 = (-b + (b**2 - 3 * a * c) ** 0.5) / (3 * a)
        lows = [-1000, min(x1, x2), max(x1, x2)]
        highs = [min(x1, x2), max(x1, x2), 1000]
    else:
        lows = [-1000]
        highs = [1000]
    for low, high in zip(lows, highs):
        if f(low) * f(high) > 0:
            continue
        if abs(f(low)) < eps:
            add_solution(low)
            continue
        if abs(f(high)) < eps:
            add_solution(high)
            continue
        mid = (low + high) / 2
        while abs(f(mid)) > eps:
            if check(high, mid):
                high = mid
            else:
                low = mid
            mid = (low + high) / 2
        add_solution(mid)

for a in ans:
    print(*a)
