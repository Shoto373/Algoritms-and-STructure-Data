import sys
sys.setrecursionlimit(10**6)
n = int(input())
roditeli = list(map(int, input().split()))

tree = [[] for _ in range(n + 1)]
koren = 1

for i in range(1, n + 1):
    rod = roditeli[i - 1]
    if rod == 0:
        koren = i
    else:
        tree[rod].append(i)

tin = [0] * (n + 1)
tout = [0] * (n + 1)
timer = [0]

def dfs(x):
    timer[0] += 1
    tin[x] = timer[0]
    for tuda in tree[x]:
        dfs(tuda)
    timer[0] += 1
    tout[x] = timer[0]

dfs(koren)

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    if tin[a] < tin[b] and tout[a] > tout[b]:
        print(1)
    else:
        print(0)
