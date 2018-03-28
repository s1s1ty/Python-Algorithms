def binary_search(s_list, key):
    start = 0
    end = len(s_list)-1

    while start <= end:
        mid = (start + end)//2

        if s_list[mid] == key:
            return True, mid

        elif s_list[mid] < key:
            start = mid + 1

        elif s_list[mid] > key:
            end = mid - 1

    return False, None