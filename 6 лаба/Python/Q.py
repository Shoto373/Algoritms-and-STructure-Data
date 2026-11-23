n, m = map(int, input().split())

matr = []
for _ in range(n):
    matr.append(list(map(int, input().split())))

hody = [(-1, 0), (1, 0), (0, -1), (0, 1)]

rasst = [[-1] * m for _ in range(n)]
rasst[0][0] = 0
q = [(0, 0)]

minnaklonov = None

for x, y in q:
    for dx, dy in hody:
        cx, cy = x, y
        popal_v_dyru = False

        while True:
            nx = cx + dx
            ny = cy + dy
            if not (0 <= nx < n and 0 <= ny < m):
                break
            if matr[nx][ny] == 1:
                break
            cx, cy = nx, ny

            if matr[cx][cy] == 2:
                popal_v_dyru = True
                break

        if popal_v_dyru:
            minnaklonov = rasst[x][y] + 1
            break

        if rasst[cx][cy] == -1:
            rasst[cx][cy] = rasst[x][y] + 1
            q.append((cx, cy))

    if minnaklonov is not None:
        break

print(minnaklonov)
