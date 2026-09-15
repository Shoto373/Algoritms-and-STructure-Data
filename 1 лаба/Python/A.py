def SelectionSort(arr):
    n = len(arr)
    for i in range(n - 1):
        max_i = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_i]:
                max_i = j
        arr[i], arr[max_i] = arr[max_i], arr[i]
    return arr


arr = list(map(int, input().split()))
print(*SelectionSort(arr))
