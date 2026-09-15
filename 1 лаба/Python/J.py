import sys

a = sys.stdin.read().split()

for i in range(1, len(a)):
    x = a[i]
    j = i - 1
    while j >= 0 and x + a[j] > a[j] + x:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = x

print("".join(a))
