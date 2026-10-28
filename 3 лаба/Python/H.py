from collections import deque

n = int(input())

left = deque()
right = deque()
ans = []

for _ in range(n):
    query = input().split()
    op = query[0]

    if op == '+':
        right.append(query[1])
    elif op == '*':
        right.appendleft(query[1])
    elif op == '-':
        ans.append(left.popleft())

   
    if len(left) < len(right):
        left.append(right.popleft())

print('\n'.join(ans))
