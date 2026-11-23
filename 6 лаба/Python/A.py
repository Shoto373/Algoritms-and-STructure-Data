n = int(input())

matr = []
for i in range(n):
    matr.append(list(map(int, input().split())))

fl = True

for i in range(n):
    for j in range(n):
        if i == j:
            if matr[i][j] != 0:
                fl = False
                break
        else:
            if matr[i][j] != matr[j][i]:
                fl = False
                break
    if not fl:
        break

if fl:
    print("YES")
else:
    print("NO")
