n, m = map(int, input().split())

gr = set()

for _ in range(m):
    x0, x1 = map(int, input().split())
    if x0 != x1:
        if x0 > x1:
            x0, x1 = x1, x0
        gr.add((x0, x1))

if len(gr) == n * (n - 1) // 2:
    print("YES")
else:
    print("NO")
