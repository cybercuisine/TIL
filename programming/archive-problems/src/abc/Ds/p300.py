from bisect import bisect_right
import math

def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0], primes[1] = False, False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i**2, n+1, i):
                primes[j] = False
    return [num for num, is_prime in enumerate(primes) if is_prime]

N = int(input())

primes = sieve_of_eratosthenes(min(N, 3 * (10 ** 5)))

cnt = 0
for i in range(len(primes)):
    a = primes[i]
    for j in range(i + 1, len(primes)):
        b = primes[j]
        if (a ** 3) * (b ** 2) > N :
            break
        c = int(math.sqrt(N / (a * a * b)))
        if c <= b:
            break
        upper = bisect_right(primes, c)
        cnt += upper - j - 1
    

print(cnt)
