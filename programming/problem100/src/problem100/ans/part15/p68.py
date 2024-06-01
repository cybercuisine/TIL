N = int(input())

n = N
ans = []
i = 2
while n > 1:
    if n % i == 0:
        ans.append(str(i))
        n //= i
    else:
        if i == 2:
            i += 1
        else:
            i += 2

print(f"{N}: {' '.join(ans)}")