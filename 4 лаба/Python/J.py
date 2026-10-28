from sys import stdin, stdout
from heapq import heappush, heappop

data = stdin.buffer.read().split()
p = 0

n = int(data[p]); p += 1
W = int(data[p]); p += 1

arr = []
for i in range(n):
    a = int(data[p]); p += 1
    w = int(data[p]); p += 1
    arr.append((a, a + w - 1, i + 1))

arr.sort()

gr = [0] * n
cnt = 0
heapp = []

for i, (l, r, num) in enumerate(arr):
    if heapp and heapp[0][0] < l:
        _, g = heappop(heapp)
        gr[i] = g
    else:
        cnt += 1
        g = cnt
        gr[i] = g
    heappush(heapp, (r, g))

res = [[] for _ in range(cnt + 1)]
for i in range(n):
    res[gr[i]].append(arr[i][2])

ans = []
for g in range(1, cnt + 1):
    ans.extend(res[g])

stdout.write(str(cnt) + '\n' + ' '.join(map(str, ans)) + '\n')
