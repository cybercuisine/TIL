import math

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N = int(input())
A = [int(input()) for i in range(N)]

dict = {}

for a in A:
    if a not in dict:
        dict[a] = 1
    else:
        dict[a] += 1


ans = 0
for key in dict.keys():
    if dict[key] >= 2:
        ans += comb(dict[key], 2)

print(ans)