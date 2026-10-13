line = input().split()
if len(line) == 1:
    n = int(line[0])
    arr = []
    while len(arr) < n:
        arr.extend(map(int, input().split()))
else:
    n = int(line[0])
    arr = list(map(int, line[1:]))

pref = [0] * (n + 1)
for i in range(n):
    pref[i + 1] = pref[i] + arr[i]

st = []
max_val = -1
best_l = 1
best_r = 1

a = arr + [-1]

for i in range(n + 1):
    while st and a[st[-1]] >= a[i]:
        h = a[st.pop()]
        if not st:
            L = 0
        else:
            L = st[-1] + 1
        R = min(i - 1, n - 1)

        total = pref[R + 1] - pref[L]
        val = h * total
        if val > max_val:
            max_val = val
            best_l = L + 1
            best_r = R + 1
    st.append(i)

print(max_val)
print(best_l, best_r)