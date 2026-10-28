import sys

class heapp:
    def __init__(self):
        self.he = [0]

    def insert(self, k):
        self.he.append(k)
        self.prosVVERH()

    def prosVVERH(self):
        he = self.he
        i = len(he) - 1
        while i > 1 and he[i] > he[i//2]:
            he[i], he[i // 2] = he[i // 2], he[i]
            i //= 2

    def prosVNIS(self):
        he = self.he
        n = len(he)
        i = 1
        while True:
            maxx = i
            if i * 2 < n and he[i * 2] > he[maxx]:
                maxx = i * 2

            if i*2 + 1 < n and he[i*2+1] > he[maxx]:
                maxx = i*2 + 1

            if maxx == i:
                break

            he[i], he[maxx] = he[maxx], he[i]
            i = maxx

    def extract(self):
        if len(self.he) <= 1:
            return None
        self.he[-1], self.he[1] = self.he[1], self.he[-1]
        pop = self.he.pop()
        if len(self.he) > 1:
            self.prosVNIS()
        return pop



Heapp = heapp()
out = []

for line in sys.stdin:
    comm = line.split()
    if not comm:
        continue
    c = comm[0]
    if c == "CLEAR":
        Heapp = heapp()
    elif c == "ADD":
        Heapp.insert(int(comm[1]))
    elif c == "EXTRACT":
        result = Heapp.extract()
        if result is not None:
            out.append(str(result))
        else:
            out.append("CANNOT")

sys.stdout.write('\n'.join(out))