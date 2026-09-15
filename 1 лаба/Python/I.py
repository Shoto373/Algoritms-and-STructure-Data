s1 = input().strip()
s2 = input().strip()

if len(s1) != len(s2):
    print("NO")
else:
    diff = {}
    for i in range(len(s1)):
        c1 = s1[i]
        c2 = s2[i]
        diff[c1] = diff.get(c1, 0) + 1
        diff[c2] = diff.get(c2, 0) - 1

    print("NO" if any(diff.values()) else "YES")
