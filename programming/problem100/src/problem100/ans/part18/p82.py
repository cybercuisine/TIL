

def convert_to_seconds(time_str):
    hh, mm, ss = map(int, time_str.split(':'))
    return hh * 3600 + mm * 60 + ss


answers = []
MAX_LENGTH = 10 ** 6

while True:
    N = int(input())
    if N == 0:
        break
    S = [0] * MAX_LENGTH
    for i in range(N):
        time = list(input().split())
        start = convert_to_seconds(time[0])
        end = convert_to_seconds(time[1])
        S[start] += 1
        S[end] -= 1
    
    for i in range(1, MAX_LENGTH):
        S[i] += S[i - 1]
    
    ans = 0
    for s in S:
        ans = max(s, ans)
    answers.append(abs(ans))  
    


print(*answers, sep='\n')