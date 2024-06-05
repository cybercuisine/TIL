A, B, K = map(int, input().split())

takahashi = A

takahashi -= min(K, A)
k = max(0, K - A)
aoki = max(B - k, 0)

print(takahashi, aoki)