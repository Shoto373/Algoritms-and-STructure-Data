n, a, b, h, w = map(int, input().split())

def can(a, b, w, h, n, d):
    rows1 = w // (a + 2 * d)
    cols1 = h // (b + 2 * d)

    rows2 = w // (b + 2 * d)
    cols2 = h // (a + 2 * d)
    return rows1 * cols1 >= n or rows2 * cols2 >= n

l = 0
r = a * b * w * h

while l + 1 < r:
    mid = (l + r) // 2
    if can(a, b, w, h, n, mid):
        l = mid
    else:
        r = mid

print(l)