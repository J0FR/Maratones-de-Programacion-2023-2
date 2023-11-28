# https://vjudge.net/contest/588342#problem/B

def dorm_water_supply(n, pipes):
    incoming = [0] * (n + 1)
    outgoing = [0] * (n + 1)
    min_diameter = {}

    for a, b, d in pipes:
        outgoing[a] = b
        incoming[b] = a
        min_diameter[(a, b)] = d

    results = []

    for tank in range(1, n + 1):
        if outgoing[tank] != 0 and incoming[tank] == 0:
            tap = tank
            diameter = float('inf')

            while outgoing[tap] != 0:
                diameter = min(diameter, min_diameter[(tap, outgoing[tap])])
                tap = outgoing[tap]

            results.append((tank, tap, diameter))

    results.sort()
    return results

n, p = map(int, input().split())
pipes = [list(map(int, input().split())) for _ in range(p)]

solution = dorm_water_supply(n, pipes)

print(len(solution))
for tank, tap, diameter in solution:
    print(tank, tap, diameter)
