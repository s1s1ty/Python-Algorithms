# Python: QuickSort


def quick_sort(arr):
    start = 0
    end = len(arr) - 1
    __quick_sort(arr, start, end)


def __quick_sort(arr, start, end):
    if start < end:
        pertition_index = __pertition(arr, start, end)
        __quick_sort(arr, start, pertition_index - 1)
        __quick_sort(arr, pertition_index + 1, end)


def __pertition(arr, start, end):
    pivot_elm = arr[end]
    pertition_index = start

    for i in range(start, end):
        if arr[i] <= pivot_elm:
            arr[i], arr[pertition_index] = arr[pertition_index], arr[i]
            pertition_index += 1

    arr[end], arr[pertition_index] = arr[pertition_index], arr[end]
    return pertition_index
