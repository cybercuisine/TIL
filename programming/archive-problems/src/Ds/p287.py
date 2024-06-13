S = input()
T = input()

SN = len(S)
N = len(T)

match = [False] * (SN)

for i in range(N):
    if i >= SN:
        break
    match[i] = (S[i] == T[i] or S[i] == '?' or T[i] == '?')
    if i > 0:
        match[i] &= match[i - 1]

match_reverse = [False] * (SN)
for i in range(N):
    if SN - i - 1 < 0:
        break
    match_reverse[i] = (S[SN - i - 1] == T[N - i - 1] or S[SN - i - 1] == '?' or T[N - i - 1] == '?')
    if i > 0:
        match_reverse[i] &= match_reverse[i - 1]

for i in range(N + 1):
    if i == 0:
        flg = match_reverse[N - 1]
    elif i == N:
        flg = match[N - 1]
    else:
        flg = match[i - 1] and match_reverse[N - i - 1]
    print("Yes" if flg else "No")
