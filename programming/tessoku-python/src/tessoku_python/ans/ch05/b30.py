def power(a, b, m):
    p = a
    ans = 1
    for i in range(30):
        wari = 2 ** i
        if (b // wari) % 2 == 1:
            ans = (ans * p) % m
        p = (p * p) % m
    return ans

def division(a, b, m):
    return (a * power(b, m-2, m)) % m

def ncr(n, r):
    m = 10 ** 9 + 7

    a = 1
    for i in range(1, n + 1):
        a = (a * i) % m

    b = 1
    for i in range(1, r + 1):
        b = (b * i) % m
    for i in range(1, n - r + 1):
        b = (b * i) % m
    
    return division(a, b, m)

h, w = map(int, input().split())
print(ncr(h + w - 2, w - 1))