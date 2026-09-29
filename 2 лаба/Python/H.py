w, h, n = map(int, input().split())

def can(n, w, h, size):
    rows = size // h
    cols = size // w
    return rows * cols >= n

l = 0
r = n * w * h

while l + 1 < r:
    mid = (l + r) // 2
    if can(n, w, h, mid):
        r = mid
    else:
        l = mid

print(r)