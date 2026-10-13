from collections import deque

p1 = deque(map(int, input().split()))
p2 = deque(map(int, input().split()))

count = 0
max_count = 10**6

while p1 and p2 and count < max_count:
    count += 1
    c1 = p1.popleft()
    c2 = p2.popleft()

    if (c1 == 0 and c2 == 9) or (c1 > c2 and not (c1 == 9 and c2 == 0)):
        p1.append(c1)
        p1.append(c2)
    else:
        p2.append(c1)
        p2.append(c2)

if not p1:
    print('second', count)
elif not p2:
    print('first', count)
else:
    print('botva')
