from sys import stdin, stdout
import bisect

def main():
    data = stdin.buffer.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1

    segs = [[1, N]]
    start_to_end = {1: N}
    end_to_start = {N: 1}
    alloc = {}
    out = []

    for i in range(1, M + 1):
        req = int(data[idx]); idx += 1

        if req > 0:
            K = req
            found = -1
            for j in range(len(segs)):
                if segs[j][1] - segs[j][0] + 1 >= K:
                    found = j
                    break

            if found == -1:
                out.append(-1)
            else:
                s, e = segs[found]
                alloc[i] = (s, s + K - 1)
                out.append(s)

                segs.pop(found)
                del start_to_end[s]
                del end_to_start[e]

                if s + K <= e:
                    ns = s + K
                    pos = bisect.bisect_left(segs, [ns])
                    segs.insert(pos, [ns, e])
                    start_to_end[ns] = e
                    end_to_start[e] = ns

        else:
            T = -req
            if T not in alloc:
                continue

            s, e = alloc[T]

            if s - 1 in end_to_start:
                ls = end_to_start[s - 1]
                pos = bisect.bisect_left(segs, [ls])
                segs.pop(pos)
                del start_to_end[ls]
                del end_to_start[s - 1]
                s = ls

            if e + 1 in start_to_end:
                re = start_to_end[e + 1]
                pos = bisect.bisect_left(segs, [e + 1])
                segs.pop(pos)
                del start_to_end[e + 1]
                del end_to_start[re]
                e = re

            pos = bisect.bisect_left(segs, [s])
            segs.insert(pos, [s, e])
            start_to_end[s] = e
            end_to_start[e] = s

    stdout.write('\n'.join(map(str, out)) + '\n')

main()
