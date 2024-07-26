from collections import defaultdict


def solve(K, A):
    freq = defaultdict(int)
    distinct_count = 0
    left = 0

    ans = 0
    for right in range(len(A)):
        freq[A[right]] += 1
        if freq[A[right]] == 1:
            distinct_count += 1

        while distinct_count > K:
            freq[A[left]] -= 1
            if freq[A[left]] == 0:
                distinct_count -= 1
            left += 1

        ans = max(right - left + 1, ans)

    return ans


def MI():
    return map(int, input().split())


N, K = MI()
A = list(MI())

print(solve(K, A))
