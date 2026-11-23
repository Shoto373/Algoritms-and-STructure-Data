n, m = map(int, input().split())

matr = []
for _ in range(n):
    matr.append(list(map(int, input().split())))

hody = [(-1, 0), (1, 0), (0, -1), (0, 1)]

rasst = [[-1] * m for _ in range(n)]
rasst[0][0] = 0
q = [(0, 0)]

for x, y in q:
    if x == n - 1 and y == m - 1:
        break
    for dx, dy in hody:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if matr[nx][ny] == 0 and rasst[nx][ny] == -1:
                rasst[nx][ny] = rasst[x][y] + 1
                q.append((nx, ny))

print(rasst[n - 1][m - 1])
