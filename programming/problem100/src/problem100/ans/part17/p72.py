import math

MOD = 10 ** 9 + 7
W, H = map(int, input().split())

print(math.comb(W + H - 2, W - 1) % MOD)