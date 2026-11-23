n = int(input())

matr = []
for _ in range(n):
    matr.append(list(map(int, input().split())))

istok = []
stok = []

for i in range(n):
    if sum(matr[row][i] for row in range(n)) == 0:
        istok.append(i + 1)
    if sum(matr[i]) == 0:
        stok.append(i + 1)

print(len(istok))
for x in istok:
    print(x)

print(len(stok))
for x in stok:
    print(x)
