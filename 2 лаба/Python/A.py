N, K = map(int, input().split())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))


for x in a2:
    l = 0
    r = N - 1
    f = False
    while l <= r:
        mid = (l + r) // 2
        if a1[mid] == x:
            f = True
            break
        elif x < a1[mid]:
            r = mid - 1
        else:
            l = mid + 1
    if f:
        print("YES")
    else:
        print("NO")