from collections import deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))

deq = deque()

for i in range(n):
    if deq and deq[0] <= i - k:
        deq.popleft()

    while deq and arr[deq[-1]] >= arr[i]:
        deq.pop()

    deq.append(i)
    if i >= k - 1:
        print(arr[deq[0]])
