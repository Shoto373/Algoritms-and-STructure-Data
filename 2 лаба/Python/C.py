C = float(input())

l = 0
r = C

for _ in range(0, 50):
    mid  = (l + r) / 2    
    if round(mid**2 + mid**0.5, 6) <= round(C, 6):
        l = mid
    else:
        r = mid

print(round(l, 6))
