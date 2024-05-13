from collections import deque

Q = int(input())

queries = [input().split() for i in range(Q)]

stack = deque()

for query in queries:
    if query[0] == "1":
        stack.append(query[1])
    elif query[0] == "2":
        print(stack[0])
    else:
        stack.popleft()