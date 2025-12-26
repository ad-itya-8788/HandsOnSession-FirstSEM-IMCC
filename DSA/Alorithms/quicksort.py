def qsort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    lesser = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return qsort(lesser) + [pivot] + qsort(greater)


arr = [44, 5, 5, 22, 3, 5, 1, 2]
print("Quick Sort:", qsort(arr))
