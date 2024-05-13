from collections import deque

S = input()

stack = deque()
ans = []

for i in range(len(S)):
    if S[i] == "(":
        stack.append(i)
    else:
        lr = [stack.pop() + 1, i + 1]
        ans.append(lr)

for a in ans:
    print(str(a[0]) + " " + str(a[1]))