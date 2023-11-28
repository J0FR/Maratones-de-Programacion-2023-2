# https://vjudge.net/contest/582424#problem/D

def longest_palindrome(s):
    def is_palindrome(check_str):
        return check_str == check_str[::-1]

    prefix = ""
    suffix = ""
    i = 0
    j = len(s) - 1
    while i < j and s[i] == s[j]:
        prefix += s[i]
        suffix = s[j] + suffix
        i += 1
        j -= 1
    
    remaining = s[i:j+1]
    longest_mid = ""
    for k in range(len(remaining) + 1):
        if is_palindrome(remaining[:k]):
            longest_mid = remaining[:k]
        if is_palindrome(remaining[-k:]):
            if k > len(longest_mid):
                longest_mid = remaining[-k:]
    return prefix + longest_mid + suffix

t = int(input())
for _ in range(t):
    s = input()
    print(longest_palindrome(s))