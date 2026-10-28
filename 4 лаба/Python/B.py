class heapp:
    def __init__(self):
        self.he=[0]

    def insert(self, k):
        self.he.append(k)
        self.prosVVERH()

    def prosVVERH(self):
        i = len(self.he) - 1
        while i > 1 and self.he[i] > self.he[i//2]:
            self.he[i], self.he[i // 2] = self.he[i // 2], self.he[i]
            i //= 2

    def prosVNIS(self):
        i = 1

        while True:
            minn = i
            if i * 2 < len(self.he) and self.he[i * 2] > self.he[minn]:
                minn = i * 2

            if i*2 + 1 < len(self.he) and  self.he[i*2+1] > self.he[minn]:
                minn = i*2 + 1

            if minn == i:
                break

            self.he[i], self.he[minn] = self.he[minn], self.he[i]
            i = minn

    def extract(self):
        self.he[-1], self.he[1] = self.he[1], self.he[-1]
        pop = self.he.pop()
        if len(self.he) > 1:
            self.prosVNIS()
        return pop

N = int(input())

Heapp = heapp()
arr = list(map(int, input().split()))
res = []

for i in range(N):
    Heapp.insert(-arr[i])

for _ in range(N):
    res.append(-Heapp.extract())
print(*res)