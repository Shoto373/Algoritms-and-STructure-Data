M, N = map(int, input().split())
T, Z, Y = [], [], []

for i in range(N):
    t, z, y = map(int, input().split())
    T.append(t)
    Z.append(z)
    Y.append(y)

def cnt(i, t):
    chel = Z[i] * T[i] + Y[i]
    f = t // chel
    o = t - f * chel
    return f * Z[i] + min(o // T[i], Z[i])

def can(t):
    s = 0
    for i in range(N):
        s += cnt(i, t)
    return s >= M

if M == 0:
    print(0)
    print(*([0] * N))
else:
    l = 0
    r = 10 ** 10

    while l + 1 < r:
        mid = (l + r) // 2
        if can(mid):
            r = mid
        else:
            l = mid

    ans = []
    s = 0
    for i in range(N):
        k = min(cnt(i, r), M - s)
        ans.append(k)
        s += k

    print(r)
    print(*ans)
