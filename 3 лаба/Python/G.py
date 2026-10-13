n = int(input())
arr = list(map(int, input().split()))


st = []
count = 1

for i in range(n):
    st.append(arr[i])
    while st and st[-1] == count:
        st.pop()
        count += 1

if not st:
    print("YES")
else:
    print("NO")
