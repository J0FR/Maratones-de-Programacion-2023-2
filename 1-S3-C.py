# https://vjudge.net/contest/578315#problem/C

def wow_factor(s):
    total = 0
    s_size = len(s)
    pref = [0] * s_size
    suff = [0] * s_size

    for i in range(1, s_size):
        suff[i] = suff[i-1]
        if s[i] == 'v' and s[i-1] == 'v':
            suff[i] += 1

    for i in range(s_size-2, -1, -1):
        pref[i] = pref[i+1]
        if s[i] == 'v' and s[i+1] == 'v':
            pref[i] += 1
            
    for i in range(s_size):
        if s[i] == 'o' and suff[i] and pref[i]:
            total += (suff[i] * pref[i])

    return total

s = input()
print(wow_factor(s))