S = input()
K = int(input())

def max_consecutive_x(S, K):
    n = len(S)
    left = 0
    right = 0
    max_x = 0
    dot_count = 0
    
    while right < n:
        if S[right] == '.':
            dot_count += 1
        
        while dot_count > K:
            if S[left] == '.':
                dot_count -= 1
            left += 1
        
        max_x = max(max_x, right - left + 1)
        right += 1
    
    return max_x

print(max_consecutive_x(S, K))
