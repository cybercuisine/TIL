from collections import defaultdict, deque

def can_change_usernames(ST):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    nodes = set()
    
    for s, t in ST:
        graph[s].append(t)
        in_degree[t] += 1
        nodes.add(s)
        nodes.add(t)
    
    queue = deque([node for node in nodes if in_degree[node] == 0])
    
    sorted_order = []
    
    while queue:
        current = queue.popleft()
        sorted_order.append(current)
        
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(sorted_order) == len(nodes):
        return True
    else:
        return False

N = int(input())
ST = [input().split() for _ in range(N)]

if can_change_usernames(ST):
    print("Yes")
else:
    print("No")
