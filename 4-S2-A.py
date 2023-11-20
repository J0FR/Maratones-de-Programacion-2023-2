# https://vjudge.net/contest/575697#problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    distr = {i: None for i in range(1, n+1)}
    for i in range(1,n+1):
        distr[i] = list(map(int, input().split()))
        distr[i].pop(0)
    matched_kingdoms = [False] * (n + 1)
    unmatched_daughter = None

    for daughter, kingdoms in distr.items():
        for kingdom in kingdoms:
            if not matched_kingdoms[kingdom]:
                matched_kingdoms[kingdom] = True
                break
        else: 
            if unmatched_daughter is None:
                unmatched_daughter = daughter

    unmatched_kingdom = None
    for kingdom in range(1, n + 1):
        if not matched_kingdoms[kingdom]:
            unmatched_kingdom = kingdom
            break

    if unmatched_daughter is not None and unmatched_kingdom is not None:
        print("IMPROVE")
        print(unmatched_daughter, unmatched_kingdom)
    else:
        print("OPTIMAL")