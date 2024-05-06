def power(a, b, m):
    p = a
    ans = 1
    for i in range(30):
        wari = 2 ** i
        if (b // wari) % 2 == 1:
            ans = (ans * p) % m
        p = (p * p) % m
    return ans

a, b = map(int, input().split())

print(power(a, b, 10**9 + 7))
