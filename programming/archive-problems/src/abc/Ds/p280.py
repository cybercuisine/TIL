from collections import defaultdict

K = int(input())

prime = defaultdict(int)
i = 2
while i * i <= K:
    while K % i == 0:
        prime[i] += 1
        K //= i
    i += 1
if K != 1:
    prime[K] += 1

ans_global = 0
for key in prime:
    ans_local = key
    cnt = prime[key]
    while True:
        tmp = ans_local
        while tmp % key == 0:
            tmp //= key
            cnt -= 1
            if cnt == 0:
                break
        if cnt == 0:
            break
        ans_local += key
    ans_global = max(ans_global, ans_local)

print(ans_global)