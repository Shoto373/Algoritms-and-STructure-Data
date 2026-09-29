a, b, c, d = map(int, input().split())

if a < 0:
    a, b, c, d = -a, -b, -c, -d

l = -10**9
r = 10**9

for _ in range(0, 50):
    mid  = (l + r) / 2    
    if round(a * mid**3 + b* mid**2 + c * mid + d, 15) <= 0:
        l = mid
    else:
        r = mid

print(round(l, 8))