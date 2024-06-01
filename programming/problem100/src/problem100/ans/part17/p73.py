def modinv(a, p):
    return pow(a, p-2, p)

def nCr_mod_p(n, r, p):
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1
    
    num = 1
    for i in range(2, n+1):
        num = (num * i) % p
    
    denom_r = 1
    for i in range(2, r+1):
        denom_r = (denom_r * i) % p
    
    denom_nr = 1
    for i in range(2, n-r+1):
        denom_nr = (denom_nr * i) % p
    
    denom_r_inv = modinv(denom_r, p)
    denom_nr_inv = modinv(denom_nr, p)
    
    result = (num * denom_r_inv % p) * denom_nr_inv % p
    return result

MOD = 10 ** 9 + 7
X, Y = map(int, input().split())

for a in range(X + 1):
    if (X - a) % 2:
        continue
    b = (X - a) // 2
    if 2 * a + b == Y:
        print(nCr_mod_p(a + b, a, MOD))
        exit()

print(0)