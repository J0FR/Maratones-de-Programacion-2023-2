# https://vjudge.net/contest/588342#problem/A

def solve_party(n, m, a, edges):
    degree = [0] * (n + 1)
    for x, y in edges:
        degree[x] += 1
        degree[y] += 1

    ans = float('inf')
    if m % 2 == 0:
        ans = 0
    else:
        for i in range(1, n + 1):
            if degree[i] % 2 == 1:
                ans = min(ans, a[i - 1])

        for x, y in edges:
            if degree[x] % 2 == 0 and degree[y] % 2 == 0:
                ans = min(ans, a[x - 1] + a[y - 1])
    return ans

casenum = int(input())
for _ in range(casenum):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    print(solve_party(n, m, a, edges))