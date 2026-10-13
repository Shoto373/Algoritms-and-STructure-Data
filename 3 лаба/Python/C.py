from collections import deque

st = deque()

vyr = input().split()

fin = 0

if vyr[0].isdigit and vyr[1].isdigit:
    for i in range(len(vyr)):
        if vyr[i].isdigit():
            st.append(vyr[i])
        else:
            y2=int(st.pop())
            y1=int(st.pop())
            fin = eval(f'{y1} {vyr[i]} {y2}')
            st.append(fin)
else:
    print('error')

print(st.pop())