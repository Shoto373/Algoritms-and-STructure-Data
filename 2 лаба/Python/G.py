N, K = map(int, input().split())

verevki = []
for ln in range(N):
    verevki.append(int(input()))

def can(verevki, K, ln):
    countVer = 0
    if ln * K <= sum(verevki):
        for x in verevki:
                if x < ln:
                    continue
                else:
                    countVer += x // ln
    return countVer >= K
                    

l = 0
r = N * max(verevki)

while l + 1 < r:
    mid = (l + r) // 2
    if can(verevki, K, mid):
        l = mid
    else:
        r = mid

print(l)