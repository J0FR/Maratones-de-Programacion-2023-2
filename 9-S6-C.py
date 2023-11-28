# https://vjudge.net/contest/588342#problem/C

from collections import deque

def bfs(graph, start, end):
    queue = deque([start])
    distances = [-1] * len(graph)
    distances[start] = 0

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    return distances[end]

def solve_two_routes(n, m, railways):
    train_graph = [[] for _ in range(n + 1)]
    bus_graph = [[] for _ in range(n + 1)]

    for u, v in railways:
        train_graph[u].append(v)
        train_graph[v].append(u)

    for u in range(1, n + 1):
        for v in range(1, n + 1):
            if u != v and v not in train_graph[u]:
                bus_graph[u].append(v)

    train_dist = bfs(train_graph, 1, n)
    bus_dist = bfs(bus_graph, 1, n)

    if train_dist == -1 or bus_dist == -1:
        return -1
    else:
        return max(train_dist, bus_dist)

n, m = map(int, input().split())
railways = [tuple(map(int, input().split())) for _ in range(m)]

result = solve_two_routes(n, m, railways)

print(result)
