from collections import defaultdict


def can_form(L, K, A):
    freq = defaultdict(int)
    distinct_count = 0
    left = 0

    for right in range(len(A)):
        freq[A[right]] += 1
        if freq[A[right]] == 1:
            distinct_count += 1

        while distinct_count > K:
            freq[A[left]] -= 1
            if freq[A[left]] == 0:
                distinct_count -= 1
            left += 1

        if right - left + 1 >= L:
            return True

    return False


def find_max_length(N, K, A):
    left, right = 1, N
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if can_form(mid, K, A):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result


def MI():
    return map(int, input().split())


N, K = MI()
A = list(MI())

print(find_max_length(N, K, A))
