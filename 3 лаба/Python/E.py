from collections import deque

class queuee:
    def __init__ (self):
        self.ar = deque()
    
    def push_front(self, n):
        self.ar.appendleft(n)
        print('ok')
    
    def push_back(self, n):
        self.ar.append(n)
        print('ok')
    
    def pop_front(self):
        if not self.ar:
            print('error')
        else:
            x = self.ar.popleft()
            print(x)
    
    def pop_back(self):
        if not self.ar:
            print('error')
        else:
            x = self.ar.pop()
            print(x)
    
    def front(self):
        if not self.ar:
            print('error')
        else:
            print(self.ar[0])

    def back(self):
        if not self.ar:
            print('error')
        else:
            print(self.ar[-1])

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
    if comm == 'push_front':
        st.push_front(int(parts[1]))
    elif comm == 'push_back':
        st.push_back(int(parts[1]))
    elif comm == 'pop_front':
        st.pop_front()
    elif comm == 'pop_back':
        st.pop_back()
    elif comm == 'front':
        st.front()
    elif comm == 'back':
        st.back()
    elif comm == 'size':
        st.size()
    elif comm == 'clear':
        st.clear()
    elif comm == 'exit':
        st.exit()
        break