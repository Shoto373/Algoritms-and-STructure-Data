n, m = map(int, input().split())

gr = [[] for _ in range(n + 1)]

for _ in range(m):
    x0, x1 = map(int, input().split())
    gr[x0].append(x1)
    gr[x1].append(x0)

posetili = [False] * (n + 1)

def dfs(x):
    posetili[x] = True
    for tuda in gr[x]:
        if not posetili[tuda]:
            dfs(tuda)

dfs(1)



if sum(posetili) == n and m == n - 1:
    print("YES")    
else:
    print("NO")
