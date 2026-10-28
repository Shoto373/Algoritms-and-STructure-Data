import heapq

heapp = []
gruz = []

N =int(input())
for i in range(N):
    T, L = map(int, input().split())
    gruz.append((T, L))
gruz.sort()

for T, L in gruz:
    if heapp and heapp[0] <= T:
        heapq.heappop(heapp)
    heapq.heappush(heapp, T + L)

print(len(heapp))