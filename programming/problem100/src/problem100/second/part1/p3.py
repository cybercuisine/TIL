S = input()

ACGT = ["A", "C", "G", "T"]

ans = 0
for i in range(len(S)):
    cnt = 0
    for j in range(i, len(S)):
        if S[j] not in ACGT:
            break
        cnt += 1
    ans = max(ans, cnt)

print(ans)