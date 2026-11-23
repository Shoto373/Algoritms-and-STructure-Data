n = int(input())

matr = []
for _ in range(n):
    matr.append(list(map(int, input().split())))

nachalo, konec = map(int, input().split())
nachalo = nachalo - 1
konec = konec - 1

if nachalo == konec:
    print(0)
    exit()

rasst = [-1] * n
pred = [-1] * n

rasst[nachalo] = 0
q = [nachalo]

for x in q:
    for tuda in range(n):
        if matr[x][tuda] == 1 and rasst[tuda] == -1:
            rasst[tuda] = rasst[x] + 1
            pred[tuda] = x
            q.append(tuda)

if rasst[konec] == -1:
    print(-1)
else:
    print(rasst[konec])
    
    putb = []
    cur = konec
    while cur != -1:
        putb.append(cur + 1)
        cur = pred[cur]
    
    print(*putb[::-1])
