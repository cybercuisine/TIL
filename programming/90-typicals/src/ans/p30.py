def sieve(N):
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, N + 1, i):
                is_prime[j] = False

    primes = [i for i in range(2, N + 1) if is_prime[i]]
    return primes


N, K = map(int, input().split())

facts = [0] * (N + 1)
primes = sieve(N)
for p in primes:
    for j in range(p, N + 1, p):
        facts[j] += 1

ans = 0
for i in range(N + 1):
    if facts[i] >= K:
        ans += 1

print(ans)
