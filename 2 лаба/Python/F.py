N, x, y = map(int, input().split())

l = -1
r = (N - 1) * max(x, y)



while l + 1 < r:
    mid = (l + r) // 2
    if (mid // x) + (mid // y) >= N - 1:
        r = mid
    else:
        l = mid

print(r + min(x, y))