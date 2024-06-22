W = int(input())

S = []
for i in range(1, 100):
    S.append(i)
    S.append(i * 100)
    S.append(i * 10000)

print(len(S))
print(*S)