def CountSort(arr):
    count = [0] * 101
    for x in arr:
        count[x] += 1

    res = []
    for i in range(101):
        while count[i] > 0:
            res.append(i)
            count[i] -= 1
    return res


arr = list(map(int, input().split()))
print(*CountSort(arr))
