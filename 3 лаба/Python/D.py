from collections import deque

class queuee:
    def __init__ (self):
        self.ar = deque()
    
    def push(self, n):
        self.ar.append(n)
        print('ok')
    
    def pop(self):
        if not self.ar:
            print('error')
        else:
            x = self.ar.popleft()
            print(x)
    
    def front(self):
        if not self.ar:
            print('error')
        else:
            print(self.ar[0])

    def size(self):
        print(len(self.ar))
    
    def clear(self):
        self.ar.clear()
        print('ok')
    
    def exit(self):
        print('bye')
        return -1

st = queuee()
while True:
    parts = input().split()
    comm = parts[0]
    if comm == 'push':
        st.push(int(parts[1]))
    elif comm == 'pop':
        st.pop()
    elif comm == 'front':
        st.front()
    elif comm == 'size':
        st.size()
    elif comm == 'clear':
        st.clear()
    elif comm == 'exit':
        st.exit()
        break