n = int(input())

matr = []
for _ in range(n):
    matr.append(list(map(int, input().split())))


cvet = [0] * n
cycl = False

def dfs(x):
    global cycl
    cvet[x] = 1
    for tuda in range(n):
        if matr[x][tuda] == 1:
            if cvet[tuda] == 1:
                cycl = True
                return
            elif cvet[tuda] == 0:
                dfs(tuda)
                if cycl:
                    return
    cvet[x] = 2

for i in range(n):
    if cvet[i] == 0:
        dfs(i)
        if cycl:
            break

if cycl:
    print(1)
else:
    print(0)
