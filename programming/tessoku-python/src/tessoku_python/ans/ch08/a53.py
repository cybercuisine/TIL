import heapq

Q = int(input())
queries = [input().split() for i in range(Q)]

products = []

for query in queries:
    if query[0] == "1":
        heapq.heappush(products, int(query[1]))
    elif query[0] == "2":
        print(products[0])
    else:
        heapq.heappop(products)
