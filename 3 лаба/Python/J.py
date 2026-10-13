t = int(input())

for _ in range(t):
    arr = list(map(float, input().split()))[1:]
    target = sorted(arr)

    st = []
    count = 0

    for i in range(len(arr)):
        st.append(arr[i])
        while st and st[-1] == target[count]:
            st.pop()
            count += 1

    if not st:
        print(1)
    else:
        print(0)

