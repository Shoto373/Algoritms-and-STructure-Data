n, m = map(int, input().split())

rebra = []
for _ in range(m):
    u, v = map(int, input().split())
    rebra.append((u, v))

perestanovka = list(map(int, input().split()))

pos = [0] * (n+1)
for i in range(n):
    pos[perestanovka[i]] = i

tosamoe = True
for u, v in rebra:
    if pos[u] >= pos[v]:
        tosamoe = False
        break

if tosamoe:
    print("YES")
else:
    print("NO")
