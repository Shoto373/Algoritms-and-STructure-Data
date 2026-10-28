import heapq

n = int(input())
col = [int(input()) for _ in range(n)]

heap = []
for i in range(n):
    t = max(1000 - col[i], 1)
    heapq.heappush(heap, (t, i, col[i]))

pos = 0
cur_t = 0

while heap:
    t_birth, aq, f = heapq.heappop(heap)

    if abs(aq - pos) <= t_birth - cur_t:
        pos = aq
        cur_t = t_birth
        nf = f + 1
        nt = t_birth + max(1000 - nf, 1)
        heapq.heappush(heap, (nt, aq, nf))
    else:
        print(t_birth)
        break
