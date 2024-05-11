N = int(input())
A = list(map(int, input().split()))

mod = [0] * 100

for i in range(N):
    mod[A[i] % 100] += 1

ans = 0
ans += mod[0] * (mod[0] - 1) // 2
ans += mod[50] * (mod[50] - 1) // 2
for i in range(1, 50):
    ans += mod[i] * mod[100-i]

print(ans)