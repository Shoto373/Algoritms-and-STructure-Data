n, s = map(int, input().split())
s = s - 1 

matr = []
for _ in range(n):
    matr.append(list(map(int, input().split())))

posetili = [False] * n

def dfs(x):
    posetili[x] = True
    for tuda in range(n):
        if matr[x][tuda] == 1 and not posetili[tuda]:
            dfs(tuda)

dfs(s)

print(sum(posetili))
