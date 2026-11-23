import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

gr = [[] for _ in range(n + 1)]

for _ in range(m):
    x0, x1 = map(int, input().split())
    gr[x0].append(x1)
    gr[x1].append(x0)

posetili = [False] * (n + 1)
res = []

def dfs(x, cur):
    posetili[x] = True
    cur.append(x)
    for tuda in gr[x]:
        if not posetili[tuda]:
            dfs(tuda, cur)

for i in range(1, n + 1):
    if not posetili[i]:
        cur = []
        dfs(i, cur)
        res.append(cur)

print(len(res))
for cur in res:
    print(len(cur))
    print(*cur)
