N, X = map(int, input().split())
S = input()

current = X

stack = []

for i in range(N):
    if S[i] == 'U':
        if stack and stack[-1] in ('L', 'R'):
            stack.pop()
        else:
            stack.append('U')
    else:
        stack.append(S[i])

for cmd in stack:
    if cmd == 'U':
        current //= 2
    elif cmd == 'L':
        current *= 2
    elif cmd == 'R':
        current = 2 * current + 1

print(current)
