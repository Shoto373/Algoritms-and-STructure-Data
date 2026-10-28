import heapq

Heapp = []
while True:
    try:

        comm = input().split()
        if not comm:
            continue
        c = comm[0]
        if c == "CLEAR":
            Heapp = []
        elif c == "ADD":
            heapq.heappush(Heapp, -int(comm[1]))
        elif c == "EXTRACT":
            if Heapp:
                print(-heapq.heappop(Heapp))
            else:
                print("CANNOT")
    except EOFError:
        break
