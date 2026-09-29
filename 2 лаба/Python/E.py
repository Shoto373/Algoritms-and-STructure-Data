N, K = map(int, input().split())
a = list(map(int, input().split()))

def can(a, k, d):
    CountzanStoyl = 1
    lastStoyl = a[0]  

    for pos in a:
        if lastStoyl + d > pos:
            continue
        else:
            CountzanStoyl += 1
            lastStoyl = pos
    return CountzanStoyl >= k
    

l = 0
r = a[-1] - a[0] + 1

while l + 1 < r:
    mid = (l + r) // 2
    if can(a, K, mid):
        l = mid
    else:
        r = mid
print(l)