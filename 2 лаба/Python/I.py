n = int(input())
a1 =  list(map(int, input().split()))

m = int(input())
a2 = list(map(int, input().split()))

a1.sort()

rescount = []
for x in a2:
    countel = 0
    l = 0
    r = n - 1
    low = n
    while l <= r:
        mid = (l + r) // 2
        if a1[mid] >= x:
            low = mid
            r = mid - 1
        else:
            l = mid + 1
    
    l = 0
    r = n - 1
    high = n
    while l <= r:
        mid = (l + r) // 2
        if a1[mid] > x:
            high = mid
            r = mid - 1
        else:
            l = mid + 1 
    rescount.append(high-low)

print(*rescount)