# https://vjudge.net/contest/589928#problem/B

def multiply_matrices(a, b, mod):
    return [
        [(a[0][0]*b[0][0] + a[0][1]*b[1][0]) % mod, (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % mod],
        [(a[1][0]*b[0][0] + a[1][1]*b[1][0]) % mod, (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % mod]
    ]

def matrix_power(matrix, power, mod):
    if power == 1:
        return matrix
    if power % 2 == 0:
        half_power = matrix_power(matrix, power // 2, mod)
        return multiply_matrices(half_power, half_power, mod)
    else:
        return multiply_matrices(matrix, matrix_power(matrix, power - 1, mod), mod)

def fibonacci_mod(n, m):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    mod = 2 ** m
    result_matrix = matrix_power([[1, 1], [1, 0]], n, mod)
    return result_matrix[0][1]

while True:
    try:
        case = input()
        if case == "":
            break
        n, m = map(int, case.split())
        print(fibonacci_mod(n, m))
    except EOFError:
        break

