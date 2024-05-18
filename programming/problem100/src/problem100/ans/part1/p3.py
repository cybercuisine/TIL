S = input()
N = len(S)

ans = 0
for i in range(N):
    for j in range(i + 1, N + 1):
        part = S[i:j]
        if part.count("A") + part.count("C") + part.count("G") + part.count("T") < len(part):
            continue
        else:
            ans = max(ans, len(part))

print(ans)