# https://vjudge.net/contest/575697#problem/D

def dfs(start_node, graph, visited, costs):
    stack = [start_node]
    min_cost = costs[start_node]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            min_cost = min(min_cost, costs[node])
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    stack.append(neighbor)
    return min_cost

n, m = map(int, input().split())
costs = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)
total_cost = 0

for i in range(1, n + 1):
    if not visited[i]:
        total_cost += dfs(i, graph, visited, costs)

print(total_cost)
