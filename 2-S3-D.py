# https://vjudge.net/contest/578315#problem/D

def c_machine(s):
    if 'm' in s or 'w' in s:
        return 0
    
    memo = [0] * (len(s) + 1)
    memo[0], memo[1] = 1, 1
    
    for i in range(2, len(s) + 1):
        if s[i-2:i] == "uu" or s[i-2:i] == "nn":
            memo[i] = (memo[i-1] + memo[i-2]) % (10**9 + 7)
        else:
            memo[i] = memo[i-1]
    return memo[len(s)]

s = input()
print(c_machine(s))