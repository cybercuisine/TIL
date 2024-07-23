S = input()
N = len(S)

sum = S.count("1")

k = N
right = N - 1
for left in range(N):
    if sum == 0 or sum == right - left + 1:
        print(k)
        exit()
    if S[left] == "1":
        sum -= 1
    if S[right] == "1" and left != right:
        sum -= 1
    k -= 1
    right -= 1
