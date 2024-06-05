N = int(input())
S = [int(input()) for _ in range(N)]

stack = []
prev = None

for i in range(N):
    s = S[i]
    if i % 2 == 1:
        if prev != s:
            stack.pop()
            if len(stack) == 0:
                stack.append(0)
    else:
        if prev != s:
            stack.append(i)
    prev = s

if prev == 0:
    stack.append(N)
if len(stack) % 2 == 1:
    stack.insert(0, 0)

print(sum(stack[1::2]) - sum(stack[::2]))