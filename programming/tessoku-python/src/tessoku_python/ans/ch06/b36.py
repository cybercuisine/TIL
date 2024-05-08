N, K = map(int, input().split())
S = input()

cnt = S.count('1')

if cnt % 2 == K % 2:
    print("Yes")
else:
    print("No")