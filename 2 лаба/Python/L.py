N, R, C = map(int, input().split())
a = []
for i in range(N):
    a.append(int(input()))

a.sort()

def can(d):
    cnt = 0
    i = 0
    while i <= N - C:
        if a[i + C - 1] - a[i] <= d:
            cnt += 1
            i += C
        else:
            i += 1
    return cnt >= R

l = -1
r = a[-1] - a[0]

while l + 1 < r:
    mid = (l + r) // 2
    if can(mid):
        r = mid
    else:
        l = mid

print(r)
