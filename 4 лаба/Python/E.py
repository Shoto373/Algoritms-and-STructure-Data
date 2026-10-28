import heapq

N = int(input())
arr = list(map(int, input().split()))

heapq.heapify(arr)

res = 0

while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    res += (a + b) * 0.05
    heapq.heappush(arr, a+b)

print(res)
