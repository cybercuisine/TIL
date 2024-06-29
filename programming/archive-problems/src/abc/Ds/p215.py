def prime_factorize(x):
    if x == 1:
        return [1]
    prime_list = []
    i = 2
    while i * i <= x:
        if x % i == 0:
            prime_list.append(i)
            x //= i
        else:
            i += 1
    if x != 1:
        prime_list.append(x)
    return prime_list


N, M = map(int, input().split())
A = list(map(int, input().split()))

prime_set = set()

for x in A:
    if x == 1:
        continue

    prime_x = prime_factorize(x)
    for p in prime_x:
        prime_set.add(p)

ans_judge = [1] * (M + 1)

for p in prime_set:
    k = 1
    while p * k <= M:
        ans_judge[p * k] = 0
        k += 1

ans = []

for i in range(1, M + 1):
    if ans_judge[i] == 1:
        ans.append(i)

print(len(ans))
for i in ans:
    print(i)
