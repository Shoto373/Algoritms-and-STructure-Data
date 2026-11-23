pos1, pos2 = input().split()

bukvy = "abcdefgh"

x1 = bukvy.index(pos1[0])
y1 = int(pos1[1]) - 1

x2 = bukvy.index(pos2[0])
y2 = int(pos2[1]) - 1

hody = [(-2, -1), (-2, 1),
    (-1, -2), (-1, 2),
    (1, -2), (1, 2),
    (2, -1), (2, 1)]

def bfs(sx, sy):
    rasst = [[-1] * 8 for _ in range(8)]
    rasst[sx][sy] = 0
    q = [(sx, sy)]
    for x, y in q:
        for dx, dy in hody:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8 and rasst[nx][ny] == -1:
                rasst[nx][ny] = rasst[x][y] + 1
                q.append((nx, ny))
    return rasst

d1 = bfs(x1, y1)
d2 = bfs(x2, y2)

minhodov = -1

for i in range(8):
    for j in range(8):
        if d1[i][j] != -1 and d1[i][j] == d2[i][j]:
            if minhodov == -1 or d1[i][j] < minhodov:
                minhodov = d1[i][j]

print(minhodov)
