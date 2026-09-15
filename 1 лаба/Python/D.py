def BubbleSort(arr):
    n = len(arr)
    count = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1
    return count


n = int(input())
arr = list(map(int, input().split()))
print(BubbleSort(arr))
