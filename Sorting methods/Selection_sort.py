def selectionSort(self, arr, n):
    l = len(arr)
    for i in range(0, l):
        min_index = i
        for j in range(i + 1, l):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
