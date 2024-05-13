Q = int(input())
queries = [input().split() for i in range(Q)]

student = {}

for query in queries:
    if query[0] == "1":
        student[query[1]] = query[2]
    else:
        print(student[query[1]])