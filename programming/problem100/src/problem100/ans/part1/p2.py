
def count_divider(n: int):
    dividers = set()
    dividers.add(n)
    
    i = 1
    while i <= n:
        if n % i == 0:
            dividers.add(i)
        i += 2
    return len(dividers)


N = int(input())
ans = []
for i in range(1, N + 1, 2):
    if count_divider(i) == 8:
        ans.append(i)

print(len(ans))