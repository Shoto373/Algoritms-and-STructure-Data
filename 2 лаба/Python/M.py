N, K = map(int, input().split())
a = []
for i in range(N):
    a.append(int(input()))

def can(ln):
    s = 0
    for x in a:
        s += x // ln
    return s >= K

l = 0
r = 10 ** 9

while l + 1 < r:
    mid = (l + r) // 2
    if can(mid):
        l = mid
    else:
        r = mid
print(l)