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
            maxx = i
            if i * 2 < len(self.he) and self.he[i * 2] > self.he[maxx]:
                maxx = i * 2

            if i*2 + 1 < len(self.he) and  self.he[i*2+1] > self.he[maxx]:
                maxx = i*2 + 1

            if maxx == i:
                break

            self.he[i], self.he[maxx] = self.he[maxx], self.he[i]
            i = maxx

    def extract(self):
        self.he[-1], self.he[1] = self.he[1], self.he[-1]
        pop = self.he.pop()
        if len(self.he) > 1:
            self.prosVNIS()
        return pop

N = int(input())

Heapp = heapp()

for _ in range(N):
    comm = input().split()

    if int(comm[0]) == 0:
        Heapp.insert(int(comm[1]))
    if int(comm[0]) == 1:
        print(Heapp.extract())