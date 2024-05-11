N, M = map(int, input().split())
A = list(map(int, input().split()))

corrects = [M] * N

for a in A:
    corrects[a-1] -= 1

for correct in corrects:
    print(correct)