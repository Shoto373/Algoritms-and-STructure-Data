class stackk:
    def __init__ (self):
        self.ar = []
    
    def push(self, n):
        self.ar.append(n)
        print('ok')
    
    def pop(self):
        if not self.ar:
            print('error')
        else:
            x = self.ar.pop()
            print(x)
    
    def back(self):
        if not self.ar:
            print('error')
        else:
            print(self.ar[-1])

    def size(self):
        print(len(self.ar))
    
    def clear(self):
        self.ar = []
        print('ok')
    
    def exit(self):
        print('bye')
        return -1

st = stackk()
while True:
    parts = input().split()
    comm = parts[0]
    if comm == 'push':
        st.push(int(parts[1]))
    elif comm == 'pop':
        st.pop()
    elif comm == 'back':
        st.back()
    elif comm == 'size':
        st.size()
    elif comm == 'clear':
        st.clear()
    elif comm == 'exit':
        st.exit()
        break