import bisect

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    p = 2

    while (p * p <= n):
        if (is_prime[p] == True):
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    prime_numbers = [p for p in range(2, n) if is_prime[p]]
    return prime_numbers



N = int(input())

UPPER = 10 ** 6 + 1
primes = sieve_of_eratosthenes(UPPER)
primes.sort()
p = len(primes) - 1

ans = 0
for i in range(len(primes)):
    while 0 < p and N < primes[i] * (primes[p] ** 3):
        p -= 1
    if p <= i:
        break
    ans += p - i

print(ans)