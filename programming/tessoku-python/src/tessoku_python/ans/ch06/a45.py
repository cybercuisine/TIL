N, C = map(str, input().split())
N = int(N)
A = input()

score = 0
for i in range(N):
    if A[i] == 'W':
        score += 0
    elif A[i] == 'B':
        score += 1
    else:
        score += 2
    score %= 3

if score == 0 and C == 'W':
    print("Yes")
elif score == 1 and C == 'B':
    print("Yes")
elif score == 2 and C == 'R':
    print("Yes")
else:
    print("No")