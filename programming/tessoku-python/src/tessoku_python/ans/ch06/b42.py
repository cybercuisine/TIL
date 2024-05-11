def solve(omote, ura, A, B):
    sum = 0
    for i in range(N):
        card1 = A[i]
        if omote == 2:
            card1 = -A[i]
        card2 = B[i]
        if ura == 2:
            card2 = -B[i]
        if card1 + card2 >= 0:
            sum += (card1 + card2)
    return sum

N = int(input())
A = [0] * N
B = [0] * N

for i in range(N):
    A[i], B[i] = map(int, input().split())

ans1 = solve(1, 1, A, B)
ans2 = solve(1, 2, A, B)
ans3 = solve(2, 1, A, B)
ans4 = solve(2, 2, A, B)

print(max(ans1, ans2, ans3, ans4))