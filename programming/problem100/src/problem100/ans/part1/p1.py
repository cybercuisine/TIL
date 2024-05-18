
answers = []

while True:
    ans = 0
    N, X = map(int, input().split())
    if N == 0 and X == 0:
        break
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            for k in range(j+ 1, N + 1):
                if i + j + k == X:
                    ans += 1
    answers.append(ans)

for ans in answers:
    print(ans)