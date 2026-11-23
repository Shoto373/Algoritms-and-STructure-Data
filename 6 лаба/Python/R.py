m, n = map(int, input().split())

matr = []
for _ in range(m):
    matr.append(list(input()))

hody = [(-1, 0), (1, 0), (0, -1), (0, 1)]

kuski = 0

for i in range(m):
    for j in range(n):
        if matr[i][j] == '#':
            kuski += 1
            q = [(i, j)]
            matr[i][j] = '.'

            for x, y in q:
                for dx, dy in hody:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and matr[nx][ny] == '#':
                        matr[nx][ny] = '.'
                        q.append((nx, ny))

print(kuski)
