n = int(input())

kuda = [0] * (n + 1)
for i in range(1, n + 1):
    kuda[i] = int(input())


cvet = [0] * (n + 1)
minkopilok = 0

for i in range(1, n + 1):
    if cvet[i] == 0:
        cur = i
        while cvet[cur] == 0:
            cvet[cur] = 1
            cur = kuda[cur]
        
        
        if cvet[cur] == 1:
            minkopilok += 1
            
        cur = i
        while cvet[cur] == 1:
            cvet[cur] = 2
            cur = kuda[cur]

print(minkopilok)
