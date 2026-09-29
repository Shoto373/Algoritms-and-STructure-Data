A, K, B, M, X = map(int, input().split())

def can(d):
    s = A * (d - d // K) + B * (d - d // M)
    return s >= X

l = 0
r = X * K * M

while l + 1 < r:
    mid = (l + r) // 2
    if can(mid):
        r = mid
    else:
        l = mid

print(r)
