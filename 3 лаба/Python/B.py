from collections import deque

st = deque()
scob = input()

for i in range(len(scob)):
    if scob[i] == ')':
        if st and st[-1] == '(':
            st.pop()
        else:
            print("no")
            break
    elif scob[i] == ']':
        if st and st[-1] == '[':
            st.pop()
        else:
            print("no")
            break
    elif scob[i] == '}':
        if st and st[-1] == '{':
            st.pop()
        else:
            print("no")
            break
    else:
        st.append(scob[i])
else:
    if not st:
        print("yes")
    else:
        print("no")
