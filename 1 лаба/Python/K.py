def make_anti_quicksort(size):
    res = list(range(1, size + 1))
    for i in range(2, size):
        m = i // 2
        res[i], res[m] = res[m], res[i]
    return res


n = int(input())
print(*make_anti_quicksort(n))
