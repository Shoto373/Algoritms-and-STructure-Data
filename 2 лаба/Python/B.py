N, K = map(int, input().split())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

for x in a2:
    l = 0
    r = N - 1

    while l + 1 < r:
        mid = (l + r) // 2
        if a1[mid] < x:
            l = mid
        else:
            r = mid      
    if abs(x - a1[l]) <= abs(x - a1[r]):
        print(a1[l])
    else:
        print(a1[r])

