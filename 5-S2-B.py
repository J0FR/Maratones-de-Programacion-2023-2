# https://vjudge.net/contest/575697#problem/B

def returnable_rooms(s):
    n = len(s)
    hasCW = '>' in s
    hasCCW = '<' in s

    if hasCW and hasCCW:
        s += s[0] 
        ans = sum(s[i] == '-' or s[i + 1] == '-' for i in range(n))
        return ans
    else:
        return n

t = int(input())
for _ in range(t):
    n = int(input())
    belts = input()
    print(returnable_rooms(belts))
