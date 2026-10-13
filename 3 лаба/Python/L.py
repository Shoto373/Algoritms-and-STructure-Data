parts = input().split()
if len(parts) == 1:
    n = int(parts[0])
    heights = list(map(int, input().split()))
else:
    n = int(parts[0])
    heights = list(map(int, parts[1:]))

s = 0
st = []

heights.append(0)

for i in range(len(heights)):
    while st and heights[st[-1]] >= heights[i]:
        h = heights[st.pop()]
        if not st:
            w = i
        else:
            w = i - st[-1] - 1
            
        if h * w > s:
            s = h * w
    st.append(i)
print(s)