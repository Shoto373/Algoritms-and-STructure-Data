n = list(map(int, input().split()))
N = n[0]
if len(n) > 1:
    arr = n[1:]


st = []

for x in arr:
   
    if st and st[-1] != x:
        k = 0
        while k < len(st) and st[-1 - k] == st[-1]:
            k += 1
        if k >= 3:
            for _ in range(k):
                st.pop()
    st.append(x)


if st:
    k = 0
    while k < len(st) and st[-1 - k] == st[-1]:
        k += 1
    if k >= 3:
        for _ in range(k):
            st.pop()

print(len(arr) - len(st))