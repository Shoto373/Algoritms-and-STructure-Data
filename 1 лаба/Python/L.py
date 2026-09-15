dist = sorted(map(int, input().split()))
fares = sorted(map(int, input().split()), reverse=True)

ans = 0
for i in range(len(dist)):
    ans += dist[i] * fares[i]

print(ans)
