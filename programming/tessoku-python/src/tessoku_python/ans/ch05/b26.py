N = int(input())

for n in range(2, N + 1):
    root = int(n ** 0.5)
    is_prime = True
    for i in range(2, root + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n)
