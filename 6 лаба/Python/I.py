n = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

hody = [(-2, -1), (-2, 1),
    (-1, -2), (-1, 2),
    (1, -2), (1, 2),
    (2, -1), (2, 1)]

rasst = [[-1] * (n + 1) for _ in range(n + 1)]
pred = [[None] * (n + 1) for _ in range(n + 1)]

rasst[x1][y1] = 0
q = [(x1, y1)]

for x, y in q:
    if x == x2 and y == y2:
        break
    for dx, dy in hody:
        nx, ny = x + dx, y + dy
        if 1 <= nx <= n and 1 <= ny <= n and rasst[nx][ny] == -1:
            rasst[nx][ny] = rasst[x][y] + 1
            pred[nx][ny] = (x, y)
            q.append((nx, ny))



putb = []
cur = (x2, y2)
while cur is not None:
    putb.append(cur)
    cur = pred[cur[0]][cur[1]]

print(rasst[x2][y2])
for x, y in putb[::-1]:
    print(x, y)
