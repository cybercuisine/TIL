N = int(input())
S = input()


ans = False
for i in range(len(S) - 2):
    if S[i] == 'R' and S[i+1] == 'R' and S[i+2] == 'R':
        ans = True
    elif S[i] == 'B' and S[i+1] == 'B' and S[i+2] == 'B':
        ans = True

if ans:
    print("Yes")
else:
    print("No")