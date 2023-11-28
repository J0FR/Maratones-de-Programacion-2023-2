# https://vjudge.net/contest/584088#problem

def where_to_turn(a, b, c):
    ab = (b[0] - a[0], b[1] - a[1])
    bc = (c[0] - b[0], c[1] - b[1])

    cross_product = ab[0] * bc[1] - ab[1] * bc[0]

    if cross_product > 0:
        return "LEFT"
    elif cross_product < 0:
        return "RIGHT"
    else:
        return "TOWARDS"

a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))
c = tuple(map(int, input().split()))

print(where_to_turn(a, b, c))