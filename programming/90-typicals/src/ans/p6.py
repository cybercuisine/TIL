def find_lexicographically_smallest_subsequence(N, K, S):
    result = []
    start = 0

    for i in range(K):
        end = N - (K - i)
        min_char = min(S[start:end + 1])
        min_index = S.index(min_char, start, end + 1)
        result.append(min_char)
        start = min_index + 1

    return "".join(result)

N, K = map(int, input().split())
S = input()

print(find_lexicographically_smallest_subsequence(N, K, S))
