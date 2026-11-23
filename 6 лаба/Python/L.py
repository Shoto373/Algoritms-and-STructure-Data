n, m = map(int, input().split())

g = [[] for _ in range(n + 1)]
for _ in range(m):
    x0, x1 = map(int, input().split())
    g[x0].append(x1)
    g[x1].append(x0)

posetili = [False] * (n + 1)
derevo_rebra = []

def dfs(x):
    posetili[x] = True
    for tuda in g[x]:
        if not posetili[tuda]:
            derevo_rebra.append((x, tuda))
            dfs(tuda)

dfs(1)

for x0, x1 in derevo_rebra:
    print(x0, x1)
