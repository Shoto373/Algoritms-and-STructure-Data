n, m = map(int, input().split())

g = [[] for _ in range(n + 1)]
for _ in range(m):
    x0, x1 = map(int, input().split())
    g[x0].append(x1)
    g[x1].append(x0)

cvet = [0] * (n + 1)
fl = True

def dfs(x, c):
    global fl
    cvet[x] = c
    drugoi_cvet = 2 if c == 1 else 1

    for tuda in g[x]:
        if cvet[tuda] == 0:
            dfs(tuda, drugoi_cvet)
        elif cvet[tuda] == c:
            fl = False

for i in range(1, n + 1):
    if cvet[i] == 0:
        dfs(i, 1)
        if not fl:
            break

if fl:
    print("YES")
    pervyi_stol = []
    for i in range(1, n + 1):
        if cvet[i] == 1:
            pervyi_stol.append(i)
    print(*pervyi_stol)
else:
    print("NO")
